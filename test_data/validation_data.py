class ValidationData:
    login_validation = {
        "credentials_error": "You have used an incorrect Username and or Password. Please review this information and try again. Or, contact your system administrator.",
        "inactive_login_error": "Your user account has been deactivated. Please contact your SilkRoad Recruiting administrator.",
        "invalid_username_password_error": "You have used an incorrect Username and or Password. Please review this information and try again. Or, contact your system administrator.",
    }

    forget_password_text = "You have requested to update your SilkRoad Recruiting password. Please provide us with the following information, so we may process your request. Once you have completed the form below and clicked the \"Submit\" button, we will send a message to the email address on file for the username provided. Please follow the directions in the message to update your password." \
                           "\nIf you do not know your username, please contact your administrator." \
                           "\n\nThank You"

    account_verification_text = "A message has been sent to your email address. Please follow the instructions in the email message to complete the change password process." \
                                "\nIf you have any questions, please contact your administrator."

    change_password_success_msg = "Your password has been changed. A confirmation of this update has been emailed to you." \
                                  "\nPlease remember to use your new password the next time you login."

    changed_password_success_email_body_text = "Hello {user} test, Your password has been changed in SilkRoad Recruiting using the \"Forgot Your Password\" feature." \
                                               " Thank you."
    sso_validation = {
        "sso_invalid_username_error": "You were not authenticated locally so SSO will not be attempted.",
        "sso_inactive_user_error": "Session Unknown"
    }
