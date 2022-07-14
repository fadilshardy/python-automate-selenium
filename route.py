import controller


def main_event(driver, event, values, window):
    """
    method to handle all event routes by main GUI
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
            driver = values[event]['driver']
            controller.update_table_gui(
                user=user, status=status, window=window, driver=driver)

        case '-UPDATE_EXCEL-':
            user = values[event]['user']
            status = values[event]['status']
            driver = values[event]['driver']
            controller.update_excel_table(
                user=user, status=status, window=window, driver=driver)

        case '-DATA_EMPTY-':
            controller.data_empty(driver=values[event])

        case '-CLOSE_APP-':
            controller.exit_app()


def setting_event(event, values, window):
    """
    method to handle all event routes by setting GUI
    """

    match event:
        case '-SAVE-':
            print(event[values])
