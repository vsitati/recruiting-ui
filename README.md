# QA Automation for Recruiting UI #

# Setup Guide

## Install Python 3:
Select the latest version from:
    
    https://www.python.org/downloads/release/python-3100/
For Windows select _Windows x86 executable installer_
        
**NB:** For Windows ensure you tick **_Add Python 3.10 to PATH_** during installation

## Verify Python and pip installation

    python --version
        Output example: Python 3.10
    pip --version
        Output example: /$ pip --version pip 22.0.4 from C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

## Create a Python virtual environment
Clone the repository.
Then in the root of the repository create the virtual environment, run:

    python3 -m venv venv

To activate the virtual environment, run from the root of the cloned repository:

    venv\Scripts\activate.bat

To deactivate the virtual environment, run:

    decativate

## Upgrade PIP(_Python package manager_)
_Activate_ the python virtual environment the run,

    python -m pip install --upgrade pip
    
## Driver management:
The drivers are all manage by the framework.
    
## Install Required Python Packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
## Executing Tests:
From the root of the repository, to run all tests:

 The following arguments are now available:

    --company(default value: qaautomationonly)   - Set the company to run tests against
    --user_role(default value: rm)               - Set the user role to execute the tests with
    --ats(default value: ats_login)              - Set the endpoint path to "/" by using the tag "ats_login" or "openadmin"
    --cx(default value: admin)                   - Set the endpoint path to "/admin" by using the tag "admin"
 
 _**NB:** All tests will run with the above default values_

    pytest

To specify a test, run:

    pytest -k <matching test name>
    

As an example: to executing all CX test, run:

_**NB:** The specified tests will run with the default values as seen above_

    pytest -k cx
For a more detailed usage of the _-k_ argument, see _pytest --help_

## Viewing Test Report:            
  To view the report, run:
  
    allure serve reporting
