import controller
from utils import helper
from gui import popup


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

        # case '-ENTRY_DATA-':
        #     user = values[event]['user']
        #     driver = values[event]['driver']
        #     controller.entry_data(
        #         user=user, window=window, driver=driver)

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


def setting_event(event, values):
    """
    method to handle all event routes by setting GUI
    """

    match event:
        case '-SAVE-':
            controller.save_setting(values)


def register_event(event, values, window, auth):
    """
    method to handle all event routes by register GUI
    """

    user_email = values['-email-']

    match event:
        case '-SUBMIT-':
            if not helper.check_if_email_valid(user_email):
                error_message = 'Input email tidak valid!'
                popup.error_popup(error_message)
                return

            confirmation_message = f'Kirim verifikasi akun dengan email {user_email}? \nJika user sudah registrasi, email tidak akan bisa diganti lagi.\nakun yang sudah di verifikasi hanya bisa digunakan oleh satu komputer.'
            confirmation = popup.confirmation_popup(confirmation_message)

            if confirmation == 'Yes':
                try:
                    auth.register_user(user_email)
                    window.write_event_value('Exit', None)

                    notification_message = f'registrasi berhasil dengan email {user_email}, kontak admin untuk validasi akun!'
                    popup.notification_pop(notification_message)

                except Exception as error:
                    popup.error_popup(error)

