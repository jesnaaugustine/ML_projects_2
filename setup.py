#convert our application to package
from setuptools import find_packages,setup
def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','') for req in requirement]
        if '-e .' in requirement:
            requirement.remove('-e .')
    return requirement

setup(
    name ='mlProject',
    version = '0.0.1',
    auther= 'Jesna',
    auther_email = 'jesnatrisa@gmail.com',
    packages=find_packages(),   #scan through entire folder and find the folder which have __init__ and create that folder as package
    install_requires=get_requirements('requirements.txt')
)