from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    This function will return the list of requirments

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPHEN_E_DOT]

        """if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)"""

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Babita',
    author_email='babita.jha6698@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
