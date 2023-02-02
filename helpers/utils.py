import os
import math
import json
import random
import randominfo
from glob import glob
from itertools import chain


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


def generate_random_person_info():
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


def get_resumes(parent_folder, specify_resume="", file_ext=""):
    """
    This function will return: A random resume, resume with specified file extension or a specified resume
    :param parent_folder: Path to the parent folder for Resumes
    :param specify_resume: Specify a specific resume
    :param file_ext: Specify a specific files extension
    """
    resume_folders = glob(os.path.abspath(f"{parent_folder}/[!_]*"))
    # [!_]: This is a regex to filter out any folder starting with an (_), for ex. __init__.py
    # TODO update this so that files can be selected from the parent folder if a sub folder does not exist
    resume_files = list(chain.from_iterable([glob(f"{resume_folder}/[!_]*") for resume_folder in resume_folders]))
    # chain.from_iterable I am using to flatten a list of lists ex. list of list looks like [[1, 2, 3], [4, 5, 6]]
    # this will be flatten to look like: [1, 2, 3, 4, 5, 6]

    if file_ext:
        try:
            return random.choice([resume_file for resume_file in resume_files if resume_file.endswith(f".{file_ext}")])
        except IndexError:
            raise BaseError(f"Specified resume with extension '{file_ext}' not found.")
    elif specify_resume:
        try:
            resume, *_ = [resume_file for resume_file in resume_files if os.path.basename(resume_file) == specify_resume]
            return resume
        except ValueError:
            raise BaseError(f"Specified resume '{specify_resume}' not found.")

    return random.choice(resume_files)


def round_up(float_number):
    """Round up a number to the nearest whole number
    :param: float number: Any float 1.2, 4.1
    """
    return math.ceil(float_number)

