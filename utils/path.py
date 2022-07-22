import os

def get_resource_path():
    """
    get absolute path to resource folder

    :return: resource path directory
    """

    current_dir = os.path.abspath(os.getcwd())

    resource_path = os.path.join(current_dir, 'resource')

    return resource_path

def get_setting_path() -> str:
    """
    get path to `setting.json` path

    :return: file path
    """

    setting_file_path = os.path.join(get_resource_path(), 'setting.json')

    return setting_file_path
