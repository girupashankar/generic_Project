#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import find_packages, setup 
from typing import List


# In[ ]:


# this function will return the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements =[]
    HYPEN_E_DOT = '-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        #remove the "\n" new line escape sequence 
        
        # remove the -e . file 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
  
    


# In[ ]:


setup(
name='mlproject',
version='0.0.1',
author='girupashankar',
author_email='girupaofficial45@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

