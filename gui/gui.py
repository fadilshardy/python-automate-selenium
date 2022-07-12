from dataclasses import dataclass

from gui.layout import layout 
import PySimpleGUI as sg

@dataclass
class Gui:
    """
    Represents main GUI class instance.
    """
    
    # --------------------- GUI LAYOUT ---------------------
    def start_gui(self):
        sg.change_look_and_feel('Light Green 1')

        window = sg.Window('Pcare BPJS', layout(),
                           icon=r'resource\icon.ico', finalize=True, modal=True, element_justification='c')
        
        return window

if __name__ == "__main__":
    try:
        gui = Gui()
        gui.start_gui()

    except Exception as e:
        print(e)
