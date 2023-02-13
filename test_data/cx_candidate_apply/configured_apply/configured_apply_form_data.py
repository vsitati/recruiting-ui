from helpers.utils import generate_random_person_info
from helpers.utils import get_resumes
import random


def phone_number():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
        n = str(random.randint(10 ** 9, 10 ** 10 - 1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


class ConfiguredApplyForm:

    def get_configured_apply_form_data(self, parent_folder, specify_resume="", file_ext=""):
        resume = get_resumes(parent_folder=parent_folder, specify_resume=specify_resume, file_ext=file_ext)
        self.fill_apply_form_data["file_path"] = resume
        return self.fill_apply_form_data()
