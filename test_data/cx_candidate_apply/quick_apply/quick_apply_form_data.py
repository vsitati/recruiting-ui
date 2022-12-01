from helpers.utils import generate_random_person_info
from helpers.utils import get_resumes


class QuickApplyForm:
    def __init__(self):
        self.form_data = generate_random_person_info()
        self.quick_apply_form_data = {
            "firstname": self.form_data.get("first_name"),
            "lastname": self.form_data.get("last_name"),
            "email": self.form_data.get("email"),
            "file_path": ""
        }

    def get_quick_apply_form_data(self, parent_folder, specify_resume="", file_ext=""):
        resume = get_resumes(parent_folder=parent_folder, specify_resume=specify_resume, file_ext=file_ext)
        self.quick_apply_form_data["file_path"] = resume
        return self.quick_apply_form_data

