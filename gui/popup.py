import PySimpleGUI as sg


def error_popup(text: str) -> None:
    """
    display popup error with given text
    """
    sg.popup_no_buttons(text, icon=r'resource\icon.ico',  auto_close=False,
                        title="Gagal!",  keep_on_top=True, background_color='#242B2E',)


def confirmation_popup(text: str) -> bool:
    """
    display confirmation popup with given text

    :return: user confirmation (bool)
    """

    confrimation = sg.popup_yes_no(
        text, title="Konfirmasi!", icon=r'resource\icon.ico')

    return confrimation


def notification_pop(text: str) -> None:
    """
    display notication popup with given text
    """
    sg.popup_no_buttons(
        text, icon=r'resource\icon.ico',  auto_close=False, title="Berhasil!",  keep_on_top=True
    )


def updating_popup(text) -> object:
    """
    initiate update popup

    :return: callable window
    """
    layout = [[sg.Text(text, font=("Calibri", 11))]]
    window = sg.Window('Please wait...', layout, no_titlebar=True,
                       keep_on_top=True, debugger_enabled=False)
    return window
