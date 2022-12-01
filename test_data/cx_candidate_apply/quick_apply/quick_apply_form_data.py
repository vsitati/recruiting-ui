from helpers.utils import get_random_person_info
import os


class QuickApplyForm:

    form_data = get_random_person_info()

    # TODO We need to add more resume files with different ext.
    # TODO Then we need to be able to select a random resume
    # TODO We must also have the ability to select a resume based on the type of ext for specific tests
    # TODO We mast pass in a list of ext to be selected

    quick_apply_form_data = {
        "firstname": form_data.get("first_name"),
        "lastname": form_data.get("last_name"),
        "email": form_data.get("email"),
        "file_path": os.path.abspath(r"test_data\resumes\docx\resume_0001.docx")
    }
