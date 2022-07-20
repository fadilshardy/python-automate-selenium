from dataclasses import dataclass

from gui.gui import Gui
from gui.setting import SettingGui
from utils.webdriver.driver import Driver
from utils.auth.firebase import Firebase

import route
import controller


@dataclass
class main:
    """
    main app
    """

    main_window = Gui().start_gui()
    driver = Driver()
    auth = Firebase()

    setting_window = SettingGui()

    def auth_guard(self):
        """
        auth guard based on user account status
        """
        user_status = self.auth.check_user()

        if not user_status:
            # popup GUI with text "you already registered on this computer with email `email`,
            # contact admin to validate your account"
            return False
        if user_status is None:
            # auth.register_user
            # Popup with register GUI
            return None
        if user_status is True:
            return True

    if auth_guard():
        while True:
            try:
                event, values = main_window.read()
                route.main_event(driver, event, values, main_window)

                if event == '-SETTING-':
                    controller.open_setting_gui(setting_window)

                if event == 'Exit' or event == 'WIN_CLOSED':
                    main_window.write_event_value('-CLOSE_APP-', driver)
                    break

            except Exception as e:
                print(e)
