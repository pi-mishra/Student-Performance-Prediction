from setuptools import find_packages,setup
from typing import list

def get_requirements(file_path:str)->list[str]:
    """
    this funtion will return the list of requirements
    """
    requirements=[]
    with open()

setup(
name= "student_performance_prediction",
version='0.0.1',
author='Piyush',
packages= find_packages()
install_requires= get_requirements('requirements.txt')
)