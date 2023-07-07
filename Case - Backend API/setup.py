# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "fly_with_us_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Fly with US",
    author_email="dummy@flywithus.org",
    url="",
    keywords=["Swagger", "Fly with US"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['fly_with_us_server=fly_with_us_server.__main__:main']},
    long_description="""\
    Fly with US analytics and employee administration -  API definition. 
    """
)
