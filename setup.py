from setuptools import setup

setup(
   name='python-automate-selenium',
   version='0.1.0',
   description='simple automation GUI for repetitive web-based tasks using selenium',
   author='Fadil S Hardy',
   author_email='fadilshrdy@gmail.com',
   packages=['python-automate-selenium'],
    install_requires=[
        'pysimplegui',
        'selenium',
        'firebase_admin',
        'cryptography',
        'chromedriver_autoinstaller',
    ]
    )