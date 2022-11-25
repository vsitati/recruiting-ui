from helpers.utils import get_random_person_info
import os


class QuickApplyForm:

    form_data = get_random_person_info()

    quick_apply_form_data = {
        "firstname": form_data.get("first_name"),
        "lastname": form_data.get("last_name"),
        "email": form_data.get("email"),
        "file_path": os.path.abspath(r"test_data\resumes\docx\resume_0001.docx")
    }
