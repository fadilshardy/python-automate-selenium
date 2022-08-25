import os
import re
import PySimpleGUI as sg

from utils import excel


def get_first_user_with_status_none_from_table_gui(datalist: list) -> list:
    """
    get first NIK with status NONE by filtering datalist from table GUI

    return None if no user with status "NONE" available

    :return: user (list)
    """

    status_index = 3

    user = next((x for x in datalist if x[status_index] == "NONE"), None)

    return user


def get_data_list_from_table_gui(window: object) -> list:
    """
    get user datalist from table GUI

    :return: user data (list)
    """
    return window['-TABLE-'].get()


def update_gui_table(user, status, window, driver) -> None:
    """
    update GUI table
    """

    datalist = get_data_list_from_table_gui(window)

    user_index = datalist.index(user)

    datalist[user_index][3] = status['success'].upper()

    window['-TABLE-'].update(values=datalist)

    window.write_event_value(
        '-UPDATE_EXCEL-', {'user': user, 'status': status, 'driver': driver})


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

    sg.Popup('No user with status NONE. check or load the data again')


def update_excel_table(user: list, status, window: object, driver: object):
    """
    update excel data by user NIK then update the excel style color
    """

    file_path = window['-LOAD_EXCEL-'].get()
    folder_path = os.path.dirname(file_path)

    file_name = os.path.basename(file_path).split('.')[0]

    email_index = 2

    user_email = user[email_index]

    df = excel.load_excel(file_path)

    excel.update_status_by_email(df, user_email, status['success'])
    excel.update_description_by_email(df, user_email, status['message'])

    styled_df = excel.update_background_color(df)
    excel.save_to_excel(
        df=styled_df, file_name=file_name, folder_path=folder_path)

    window.write_event_value('-AUTOMATE_LOOP-', driver)


def is_file_writeable(file_path: str):
    """
    workaround to check if file is writeable or not ***WINDOWS ONLY***
    """

    folder_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path).split('.')[0]

    original_file = f'{folder_path}/{file_name}.xlsx'
    temporary_file = f'{folder_path}/{file_name}_temp.xlsx'

    try:
        os.rename(original_file, temporary_file)
        os.rename(temporary_file, original_file)

        return True

    except OSError:
        error_popup = sg.Popup(
            'Error!', f'file is not editable, close any app that are using {file_name}')

        if error_popup == 'ok':
            return False


def check_if_email_valid(email):
    """
    check if email address is in a valid format using re.match

    :return: is_valid (bool)
    """

    is_valid = re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)

    if is_valid is None:
        return False

    return True


def get_user_by_email_from_excel(window, user):
    """
    get user data by email from excel

    :return: user (list)
    """

    file_path = window['-LOAD_EXCEL-'].get()

    dataframe = excel.load_excel(file_path)

    email_index = 2

    user = excel.get_column_by_email(dataframe, user[email_index])

    return user.to_dict('list')
