import PySimpleGUI as sg


def layout() -> list:
    """
    GUI layout

    :return: list
    """
    data = []
    header_list = ['PSNOKA_BPJS', 'NAMA INDIVIDU', '  STATUS  ']

    layouts = [
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

        [sg.Button('Start',  key='-START-', disabled=True), sg.Button('Setting',  key='-SETTING-', disabled=True), sg.Button('Exit')], ]

    return layouts
