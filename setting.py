
import os
import json
from dataclasses import dataclass

import route
from utils import path, crypt

from gui.setting_gui import SettingGui


@dataclass
class Setting:
    """
    Represents setting class instance.
    """


    setting_file_path: str = os.path.join(path.get_resource_path(), 'setting.json')

    def get_setting(self):
        """
        get setting data from encrypted `setting.json`

        :return: decrypted setting json
        """

        key = crypt.load_key()

        decrypted_setting = crypt.decrypt_to_bytes(self.setting_file_path, key)

        settings = json.loads(decrypted_setting)

        return settings



    def open_setting_gui(self):
        """
        initiate setting GUI
        """
        setting_data = self.get_setting()

        setting_window = SettingGui().start_gui(setting_data)

        try:
            event, values = setting_window.read()
            setting_window.close()

            route.setting_event(event, values)

            if event in ('Exit', 'WIN_CLOSED', None):
                setting_window.close()
                del setting_window

        except Exception as error:
            print(error)


if __name__ == "__main__":
    try:
        setting = Setting()

        setting.open_setting_gui()

    except Exception as e:
        print(e)