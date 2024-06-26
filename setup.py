from setuptools import setup,find_packages
from typing import List 


#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Talloji Harshith"

REQUIREMENTS_FILE_NAME="requirements.txt"
def get_requirements_list()->List[str]:
    """
    Description: This function basically returns the list which contains name of libraries from requirements.txt
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=get_requirements_list()

)

