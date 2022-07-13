import os

import PySimpleGUI as sg

from utils import excel


def get_first_user_with_status_none_from_table(datalist: list) -> list:
    """
    get first NIK with status NONE by filtering datalist from table GUI

    return None if no user with status "NONE" available

    :return: user (list)
    """

    user = next((x for x in datalist if x[2] == "NONE"), None)

    return user


def get_data_list_from_table_gui(window: object) -> list:
    """
    get user datalist from table GUI

    :return: user data (list)
    """
    return window['-TABLE-'].get()


def update_gui_table(user, status, window) -> None:
    """
    update GUI table
    """

    datalist = get_data_list_from_table_gui(window)

    user_index = datalist.index(user)

    datalist[user_index][2] = status['success'].upper()

    window['-TABLE-'].update(values=datalist)


def rows_input_popup() -> int:
    """
    display a popup for excel rows

    :return: rows (int)
    """
    rows_count = sg.popup_get_text(
        'how many rows?', no_titlebar=True, keep_on_top=True)

    if not rows_count:
        rows_count = 10

    return int(rows_count)


def empty_popup() -> None:
    """
    display  a popup if datalist has no user by status NONE
    """

    sg.Popup('Tidak ada user dengan status NONE. check atau load ulang data')


def update_excel_table(user: list, status, window: object):
    """
    update excel data by user NIK then update the excel style color
    """

    file_path = window['-LOAD_EXCEL-'].get()
    folder_path = os.path.dirname(file_path)

    file_name = os.path.basename(file_path).split('.')[0]

    user_nik = user[0]

    original_file = f'{folder_path}/{file_name}.xlsx'
    temporary_file = f'{folder_path}/{file_name}_temp.xlsx'

    df = excel.load_excel(file_path)
    while True:
        try:
            # workaround to check if file is writeable or not ***WINDOWS ONLY***
            os.rename(original_file, temporary_file)
            os.rename(temporary_file, original_file)

            excel.update_status_by_nik(df, user_nik, status['success'])
            excel.update_description_by_nik(df, user_nik, status['message'])

            styled_df = excel.update_background_color(df)
            excel.save_to_excel(
                df=styled_df, file_name=file_name, folder_path=folder_path)
            break
        except OSError:
            error_alert = sg.Popup(
                'Error!', f'file tidak bisa diedit, tutup aplikasi yang membuka file {file_name}')
            if error_alert == 'ok':
                continue
