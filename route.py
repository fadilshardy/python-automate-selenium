import controller 
import PySimpleGUI as sg

def gui_event(driver, event, values, window):
    match event:
        case "-START-":
            controller.login_app(driver, window)
        case "-LOAD_EXCEL-":
            rows = sg.popup_get_text('rows?', no_titlebar=True, keep_on_top=True)
            
            if(rows is None):
                rows = 10
                
            controller.load_excel_to_gui(values, window, int(rows))
        case "-AUTOMATE-":
            driverInstance = values["-AUTOMATE-"]
            controller.automate_input(driverInstance, window)


            

