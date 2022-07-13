import PySimpleGUI as sg
from numpy import row_stack


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
