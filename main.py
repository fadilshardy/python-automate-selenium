from dataclasses import dataclass

from gui.gui import Gui

@dataclass
class main:
    # driver = Driver().get_driver()

    window = Gui().start_gui()
    
    while True:
        try:
            event, values = window.read()
            
            if event == "Exit":
                break
            
        except Exception as e:
            print(e)

git 