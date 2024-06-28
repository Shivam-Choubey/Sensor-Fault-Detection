from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns the list of requirements
    """
    requirements_list: List[str] = []

    return requirements_list

setup(
    name="Sensor",
    version="0.0.1",
    author="Shivam_Choubey",
    author_email="shivamchoubey8838@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(), #["pymongo==4.2.0"],
)
