from setuptools import setup, find_packages

setup(
    name='protos',
    version='0.1.2',
    packages=find_packages(where="gen/python"), 
    include_package_data=True,  
    py_modules=['protos'],   
    package_dir={"": "gen/python"},   
)
