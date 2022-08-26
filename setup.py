from setuptools import setup

setup(
   name='webinput-automation-gui',
   version='0.1.0',
   description='simple automation input GUI for repetitive web-based tasks using selenium',
   author='Fadil S Hardy',
   author_email='fadilshrdy@gmail.com',
   packages=['webinput-automation-gui'],
    install_requires=[
        'pysimplegui',
        'selenium',
        'firebase_admin',
        'cryptography',
        'chromedriver_autoinstaller',
        'jinja2',
        'pandas'
    ]
    )