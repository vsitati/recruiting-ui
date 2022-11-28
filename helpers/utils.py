import os
import json
import random
import randominfo


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


class BaseError(Exception):
    pass


def get_random_person_info():
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance",
               "company", "corporation", "community"]
    extensions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site',
                  'xyz', 'zero', 'tech']

    first_name = randominfo.get_first_name()
    last_name = randominfo.get_last_name()

    return dict(
        first_name=first_name,
        last_name=last_name,
        email=f"{first_name}.{last_name}@{random.choice(domains)}.{random.choice(extensions)}"
    )


def get_basename_from_file_path(file_path):
    return os.path.basename(file_path)
