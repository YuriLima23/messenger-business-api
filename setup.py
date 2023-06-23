import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='messenger-business-api',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='This repository is a wrapper for Meta messenger api for Messenger and Instagram',
    long_description=README,
    author='Yuri Ramos Lima',
    author_email='yurilima93@hotmail.com',
    keywords=['python','Meta', 'Facebook', 'Instagram', 'message', 'chat-bot'],
    python_requires='>=3',
    zip_safe=False,
    install_requires=[ 'pydantic', 'requests'],
)
