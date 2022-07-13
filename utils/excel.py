import pandas as pd


def load_excel(excel_path: str) -> list:
    """
    load the excel file to pandas dataframe.

    :return: dataframe list
    """
    df = pd.read_excel(excel_path)

    if 'STATUS' not in df:
        df = df.assign(STATUS="NONE")
    if 'DESCRIPTION' not in df:
        df = df.assign(DESCRIPTION=None)

    return df


def add_status_column_to_excel(excel_path: str) -> list:
    """
    add status column to dataframe

    :return: dataframe list
    """

    df = load_excel(excel_path)

    new_df = df.assign(STATUS="NONE")

    new_df.to_excel('converted.xlsx', index=False)

    return new_df


def update_background_color(df: object) -> object:
    """
    update background color of the dataframe based on status row.

    :return: updated dataframe list
    """

    def row_style(row):
        if row['STATUS'] == "NONE":
            return ['background-color: #B3B6B7'] * len(row)
        if row['STATUS'] == "BERHASIL":
            return ['background-color: #239B56'] * len(row)
        if row['STATUS'] == "GAGAL":
            return ['background-color: #B03A2E'] * len(row)
        if row['STATUS'] == "TIDAK AKTIF":
            return ['background-color: #283747'] * len(row)
        return ['background-color: #FBF8F1'] * len(row)

    updated_df = df.style\
        .apply(row_style, axis=1)

    return updated_df


def save_to_excel(df: object, file_name: str = 'output', folder_path: str = '') -> object:
    """
    save dataframe to excel file

    :return: saved dataframe
    """

    file_path = f'{folder_path}/{file_name}'

    df.to_excel(f'{file_path}.xlsx', index=False)

    return df


def get_columns_by_status(df: object, status: str) -> object:
    """
    filter columns of dataframe by status

    :return: filtered dataframe object
    """

    columns_by_status = df.loc[df['STATUS'] == status.upper()]

    return columns_by_status


def get_column_by_nik(df: object, nik: int) -> object:
    """
    filter columns of dataframe by nik

    :return: filtered dataframe object
    """

    columns_by_nik = df.loc[df['PSNOKA_BPJS'] == nik]

    return columns_by_nik


def get_first_nik_column_by_status_none(df: object) -> int:
    """
    get first column of dataframe with status none

    :return: first column of dataframe nik number (int)
    """

    columns_by_status = get_columns_by_status(df, status='none')

    first_column = columns_by_status.iloc[0]

    first_column_nik = first_column['PSNOKA_BPJS']

    return int(first_column_nik)


def update_description_by_nik(df: object, nik: int, description: str) -> object:
    """
    update description of dataframe column filtered by nik with given status

    :return: updated dataframe column
    """

    df.loc[df['PSNOKA_BPJS'] == nik, 'DESCRIPTION'] = description

    return df


def update_status_by_nik(df: object, nik: int, status: str) -> object:
    """
    update status of dataframe column filtered by nik with given status

    :return: updated dataframe column
    """

    df.loc[df['PSNOKA_BPJS'] == nik, 'STATUS'] = status.upper()

    return df
