from dataclasses import dataclass

from gui.main_gui import Gui
# from auth import Auth
from setting import Setting
from utils.webdriver.driver import Driver

import route


@dataclass
class Main:
    """
    main app
    """

    def start_app(self):
        """
        start main app instance
        """
        main_window = Gui().start_gui()

        driver = Driver()
        while True:
            try:
                event, values = main_window.read()
                route.main_event(driver, event, values, main_window)

                if event == '-SETTING-':
                    setting = Setting()
                    setting.open_setting_gui()

                if event in ('Exit', 'WIN_CLOSED'):
                    main_window.write_event_value('-CLOSE_APP-', driver)
                    break

            except Exception as error:
                print(error)


if __name__ == "__main__":
    try:
        # auth = Auth()
        main = Main()

        # if auth.check():
        #     main.start_app()
        main.start_app()
    except Exception as e:
        print(e, )
