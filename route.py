import controller


def gui_event(driver, event, values, window):
    """
    method to handle all event routes by the GUI
    """
    match event:
        case '-START-':
            controller.login_app(driver, window)
        case '-LOAD_EXCEL-':
            controller.load_excel_to_gui(values, window)
        case '-AUTOMATE-':
            user = values[event]['user']
            driver = values[event]['driver']
            controller.automate_input(driver=driver, user=user, window=window)
        case '-AUTOMATE_LOOP-':
            driver = values[event]
            controller.automate_loop(driver, window)

        case '-UPDATE_TABLE-':
            user = values[event]['user']
            status = values[event]['status']
            controller.update_table_gui(user, status, window)
        case '-DATA_EMPTY-':
            controller.data_empty(driver=values[event])
