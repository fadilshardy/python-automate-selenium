from dataclasses import dataclass
import PySimpleGUI as sg

from gui.layout import main_layout


@dataclass
class Gui:
    """
    Represents main GUI class instance.
    """

    # --------------------- GUI LAYOUT ---------------------
    def start_gui(self) -> object:
        """
        method to initiate GUI

        :return: pysimplegui window instance
        """
        sg.change_look_and_feel('darkBlack')

        window = sg.Window('Pcare BPJS', main_layout(),
                           icon=r'resource\icon.ico',
                           finalize=True,
                           modal=True,
                           element_justification='c')

        return window


if __name__ == "__main__":
    try:
        gui = Gui()
        gui.start_gui()

    except Exception as e:
        print(e)
