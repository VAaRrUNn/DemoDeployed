from setuptools import find_packages, setup 
from typing import List


HYPEN_E = '-e .'
def get_requirements(file_path: str) -> List:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", '') for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements


setup(
name="Demo ML Project",
version="0.0.1",
author="Varun",
author_email="sanatoo.varun666@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),
)