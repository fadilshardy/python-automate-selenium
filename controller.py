import os
import sys
import threading

from utils import excel
from utils import helper

from modules.bpjs import login
from modules.bpjs import search_user


def exit_app():
    """
    method to force close driver & main app instance.
    """

    os.system("taskkill /f /im  driver.exe")
    os.system("taskkill /f /im  pcare-vaksin.exe")

    sys.exit()


def login_app(driver, window):
    """
    Method to login the website
    """
    driver_instance = driver.get_driver()

    threading.Thread(target=login.login_website, args=(
        driver_instance, window,),  daemon=True).start()


def load_excel_to_gui(values, window):
    """
    Method to load excel to GUI
    """

    rows_count = helper.rows_input_popup()

    file_path = values['-LOAD_EXCEL-']
    df = excel.load_excel(file_path)

    df_status_none = excel.get_columns_by_status(
        df, status="NONE").head(rows_count)
    data = df_status_none[['PSNOKA_BPJS',
                           'NAMA INDIVIDU', 'STATUS']].values.tolist()

    window['-TABLE-'].update(values=data)
    window['-START-'].update(disabled=False)


def automate_input(user, driver, window):
    """
    Method to automate data to website
    """

    threading.Thread(target=search_user.search, args=(
        user, driver, window, ),  daemon=True).start()


def update_table_gui(user: list, status: list, window: object) -> None:
    """
    Method to update table on GUI
    """

    helper.update_gui_table(user=user, status=status, window=window)


def automate_loop(driver, window):
    """
    main automation loop, input if user by status None is available from table GUI
    """

    datalist = window['-TABLE-'].get()

    user = helper.get_first_user_with_status_none_from_table(datalist)

    if user is None:
        print('data kosong')
        return window.write_event_value('-DATA_EMPTY-', 'empty')

    window.write_event_value(
        '-AUTOMATE-', {'driver': driver, 'user': user})


def data_empty():
    """
    Method to handle if data user by status NONE is empty
    """

    helper.empty_popup()
