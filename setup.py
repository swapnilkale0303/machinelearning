from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
  """
  this function will return the list of get_requirments
  
  """
  
  hypen_e_dot="-e ."
  
  get_requirments=[]
  with open(file_path) as file_obj:
    requirments=file_obj.readlines()
    requirments=[req.replace("\n","") for req in requirments]
  
  
    if  hypen_e_dot in requirments:
        requirments.remove(hypen_e_dot)

    return requirments
    
setup(
  
name="mlprojects",
version='0.0.1',
author='krish',
author_email='sskale0607@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')    
    
    
)