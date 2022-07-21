import PySimpleGUI as sg


def main_layout() -> list:
    """
    main GUI layout

    :return: list
    """
    data = []
    header_list = ['PSNOKA_BPJS', 'NAMA INDIVIDU', '  STATUS  ']

    layout = [
        [sg.FileBrowse('Load Excel', key="-PATH-", target='-LOAD_EXCEL-',  file_types=((".xlsx, xls, CSV", ["*.xlsx", "*.xls", "*.csv", ]),)),
         sg.Input('', key="-LOAD_EXCEL-", enable_events=True, disabled=True)],
        [sg.Table(values=data,
                  key="-TABLE-",
                  headings=header_list,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  background_color='lightblue',
                  alternating_row_color='lightyellow',
                  hide_vertical_scroll=False,
                  visible=True,
                  justification='center',

                  num_rows=25)],

        [sg.Button('Start',  key='-START-', disabled=True), sg.Button('Setting',  key='-SETTING-', disabled=False), sg.Button('Exit')], ]

    return layout


def setting_layout() -> list:
    """
    setting GUI layout

    :return: list
    """
    setting = {'-username-': 'test', '-password-': '****'}  # get_setting()

    layout = [
        [
            sg.Text("Username", size=(20, 1)),
            sg.InputText(default_text=setting['-username-'],
                         size=(20, 1),
                         key='-username-'),
        ],
        [
            sg.Text("Password", size=(20, 1)),
            sg.InputText(default_text=setting['-password-'],
                         size=(20, 1),
                         key='-password-'),
        ],
        [sg.Button('Start',  key='-START-', disabled=True), sg.Button('Setting',
                                                                      key='-SETTING-', disabled=False), sg.Button('Exit')],
    ]

    return layout


def register_layout() -> list:
    """
    register GUI layout

    :return: list
    """

    layout = [
    [sg.Text("Email", size=(15, 1), font=16),
        sg.InputText(key='-email-', font=16)],
    [sg.Button("-SUBMIT-")]]

    return layout
