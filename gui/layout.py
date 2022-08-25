import PySimpleGUI as sg


def main_layout() -> list:
    """
    main GUI layout

    :return: list
    """
    data = []
    header_list = [' ID ',
                   'First name', 'Email', ' Status ']
    sg.theme('darkBlack')

    layout = [
        [sg.FileBrowse('Load Excel', key="-PATH-",  target='-LOAD_EXCEL-',  file_types=((".xlsx, xls, CSV", ["*.xlsx", "*.xls", "*.csv", ]),)),
         sg.Input('', key="-LOAD_EXCEL-", enable_events=True, disabled=True, disabled_readonly_text_color="black")],
        [sg.Table(values=data,
                  key="-TABLE-",
                  headings=header_list,
                  display_row_numbers=False,
                  auto_size_columns=False,
                  col_widths=[5, 10, 20, 10],
                  background_color='black',
                  alternating_row_color='gray',
                  hide_vertical_scroll=False,
                  visible=True,
                  justification='center',
                  num_rows=25)],

        [sg.Button('Start',  key='-START-', disabled=True), sg.Button('Setting',  key='-SETTING-', disabled=False), sg.Button('Exit')], ]

    return layout


def setting_layout(setting_data) -> list:
    """
    setting GUI layout

    :return: list
    """

    layout = [
        [
            sg.Text("Username", size=(20, 1)),
            sg.InputText(default_text=setting_data['username'],
                         size=(20, 1),
                         key='username'),
        ],
        [
            sg.Text("Password", size=(20, 1)),
            sg.InputText(default_text=setting_data['password'],
                         size=(20, 1),
                         key='password'),
        ],
        [sg.Button('Save',  key='-SAVE-'), sg.Button('Exit')],
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
