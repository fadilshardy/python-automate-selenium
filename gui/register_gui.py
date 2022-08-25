from dataclasses import dataclass
import PySimpleGUI as sg

from gui import layout


@dataclass
class RegisterGui:
    """
    Represents setting GUI class instance.
    """

    # --------------------- GUI LAYOUT ---------------------
    def start_gui(self) -> object:
        """
        method to initiate GUI

        :return: pysimplegui window instance
        """

        window = sg.Window('register account', layout.register_layout(),
                           icon=r'resource\icon.ico', finalize=True, modal=True, element_justification='c')

        return window


if __name__ == "__main__":
    try:
        gui = RegisterGui()
        gui.start_gui()

    except Exception as e:
        print(e)
