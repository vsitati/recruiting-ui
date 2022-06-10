import os
import json


def get_config(config_path):
    """
    Load a JSON file.
    :param config_path: Path to the json file.
    :return: A dictionary.
    """
    config_file = open(config_path)
    return json.load(config_file)


def create_folder(folder_name):
    """
    Create a given folder if it does not exist.
    :param folder_name: The folder's name to be created
    """
    if not os.path.exists(folder_name):
        return os.makedirs(folder_name)
    return True
