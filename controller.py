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
    driverInstance = driver.get_driver()
    
    threading.Thread(target=login.login_website, args=(
                        driverInstance, window,),  daemon=True).start()   


def load_excel_to_gui(values, window, rows):
    """
    Method to load excel to GUI
    """
    
    file_path = values['-LOAD_EXCEL-']
    df = excel.load_excel(file_path)
    
    df_status_none = excel.get_columns_by_status(df, status="NONE").head(rows)
    data = df_status_none[['PSNOKA_BPJS', 'NAMA INDIVIDU', 'STATUS']].values.tolist() 
    

    window['-TABLE-'].update(values=data)
    window['-START-'].update(disabled=False)
    
def automate_input(driver, window):
    """ 
    Method to automate data to website
    """
    
    while True:
        try:
            datalist = window['-TABLE-'].get()

            user = helper.get_first_user_with_status_none_from_table(datalist)
            
            
            if(user is None):
                print('data kosong')
                break
            
            NIK = int(user[0])

            result = search_user.search(nik=NIK, driver=driver, window=window)
                        
            if(result['success']):
                status = 'BERHASIL'
            else:
                status='GAGAL'
            
            helper.update_gui_table(datalist=datalist, user=user, status=status, window=window)
        except Exception as e:
            print(e)


