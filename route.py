import controller 

def gui_event(driver, event, values, window):
    match event:
        case "-START-":
            controller.login_app(driver, window)
        case "-LOAD_EXCEL-":
            controller.load_excel_to_gui(values, window)
         

            

