import os
import sys
import threading
import json
import PySimpleGUI as sg

from gui import popup

from utils import excel, helper, crypt, path

from modules.bpjs import login
from modules.bpjs import search_user


def exit_app():
    """
    method to force close driver & main app instance.
    """
    os.system("taskkill /f /im  pcare-bpjs.exe")

    os.system("taskkill /f /im  chromedriver.exe")

    sys.exit()


def login_app(driver, window):
    """
    Method to login the website
    """
    driver_instance = driver.get_driver()

    window['-START-'].update(disabled=True)

    threading.Thread(target=login.login_website, args=(
        driver_instance, window,),  daemon=True).start()


def load_excel_to_gui(values, window):
    """
    Method to load excel to GUI
    """

    rows_count = helper.rows_input_popup()

    file_path = values['-LOAD_EXCEL-']

    if not helper.is_file_writeable(file_path):
        return None

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


def update_table_gui(user: list, status: list, window: object, driver: object) -> None:
    """
    Method to update table on GUI
    """

    threading.Thread(target=helper.update_gui_table, args=(
        user, status, window, driver,),  daemon=True).start()


def update_excel_table(user: list, status: list, window: object, driver: object) -> None:
    """
    Method to update table on excel
    """

    popup_text = 'mengupdate excel... \njangan tutup aplikasi'

    sg.popup_auto_close(popup_text, no_titlebar=True,
                        keep_on_top=True, button_type=5)

    threading.Thread(target=helper.update_excel_table, args=(
        user, status, window, driver),  daemon=True).start()



def automate_loop(driver, window):
    """
    main automation loop, entry data if user by status `none` is available from table GUI
    """

    datalist = window['-TABLE-'].get()

    user = helper.get_first_user_with_status_none_from_table_gui(datalist)

    if user is None:
        return window.write_event_value('-DATA_EMPTY-', driver)

    window.write_event_value(
        '-AUTOMATE-', {'driver': driver, 'user': user})


def data_empty(driver: object):
    """
    Method to handle if data user by status NONE is empty
    """

    driver.quit()

    helper.empty_popup()


def save_setting(setting_data):
    """
    save setting data to `setting.json` and encrypt it.
    """

    key = crypt.load_key()

    with open(path.get_setting_path(), "w", encoding="utf-8") as write_file:
        json.dump(setting_data, write_file, indent=1)

    crypt.encrypt_file(path.get_setting_path(), key)
