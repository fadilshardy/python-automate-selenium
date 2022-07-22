from dataclasses import dataclass
import PySimpleGUI as sg

from gui import layout


@dataclass
class SettingGui:
    """
    Represents setting GUI class instance.
    """

    # --------------------- GUI LAYOUT ---------------------
    def start_gui(self, setting_data: str) -> object:
        """
        method to initiate GUI

        :return: pysimplegui window instance
        """
        sg.change_look_and_feel('Light Green 1')

        window = sg.Window('Pcare BPJS', layout.setting_layout(setting_data),
                           icon=r'resource\icon.ico', finalize=True, modal=True, element_justification='c')

        return window


if __name__ == "__main__":
    try:
        gui = SettingGui()

    except Exception as e:
        print(e)
