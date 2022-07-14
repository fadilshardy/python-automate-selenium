from dataclasses import dataclass

from gui.gui import Gui
from gui.setting import SettingGui
from utils.webdriver.driver import Driver
import route
import controller


@dataclass
class main:
    """
    main app
    """

    main_window = Gui().start_gui()
    driver = Driver()

    setting_window = SettingGui()

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
