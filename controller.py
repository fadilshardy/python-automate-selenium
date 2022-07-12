import os
import sys

from modules.bpjs import login
from utils import excel 

def exit_app():
    """
    method to force close driver & main app instance.
    """
    
    os.system("taskkill /f /im  driver.exe")
    os.system("taskkill /f /im  pcare-vaksin.exe")

    sys.exit()

def login_app(driver, window):
    """
    Method to login the app
    """
        
    login.login_website(driver.get_driver(), window)


def load_excel_to_gui(values, window):
    """
    Method to load excel to GUI
    """
    file_path = values['-LOAD_EXCEL-']
    df = excel.load_excel(file_path)
    data = df[['PSNOKA_BPJS', 'NAMA INDIVIDU', 'STATUS']].values.tolist() 

    window['-TABLE-'].update(values=data)
    window['-START-'].update(disabled=False)
