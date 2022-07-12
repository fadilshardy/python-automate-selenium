import os

def get_resource_path():
    """
        get absolute path to resource folder

        :return: resource path directory
        """

    current_dir = os.path.abspath(os.getcwd())

    resource_path = os.path.join(current_dir, 'resource')

    return resource_path
