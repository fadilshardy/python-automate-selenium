from dataclasses import dataclass

from gui.gui import Gui
from utils.webdriver.driver import Driver
import route


@dataclass
class main:
    """
    main app
    """

    window = Gui().start_gui()
    driver = Driver()

    while True:
        try:
            event, values = window.read()

            route.gui_event(driver, event, values, window)
            if event == "Exit":
                break

        except Exception as e:
            print(e)
