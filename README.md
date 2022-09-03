## **Project Description**

Simple python desktop application for automating repetitive web-based input tasks which load the data from a spreadsheet. developed using selenium as webdriver and pysimplegui as GUI

[live demo](https://www.youtube.com/watch?v=tIiq2KftbTM) | [read more](https://fadilshardy.vercel.app/blog/python-webinput-automation-gui-with-selenium-and-pysimplegui) about the project

## How to install

Make sure you have [Python 3.10](https://www.python.org/downloads/windows/) and pip installed, then get necessary packages by running `pip install -r requires.txt`

run the following scripts to comple into an executable file using nuitka.

```
nuitka main.py  --include-data-dir=resource=resource/  --run --onefile --include-package-data=selenium,pysimplegui,pandas,jinja2   --include-package=jinja2 --enable-plugin=tk-inter,numpy  --windows-icon-from-ico=resource/icon.ico  --noinclude-pytest-mode=nofollow --noinclude-setuptools-mode=nofollow --output-dir=build/ --clang --mingw64 --windows-disable-console
```

Depending on your computer, this might take some time.

As of now the app only tested on windows OS.

## `<b>`encrypt data

simple helper to encrypt/decrpyt to prevent user from modifying sensitive data.
how to use:

```
py -m utils.crypt **args
```

usage:

```
generate key:
    py -m utils.crypt -g

encrypt file with given filepath:
    py -m utils.crypt -e -file_path=RELATIVE_FILE_PATH

decrypt file with given filepath:
    py -m utils.crypt -d -file_path=RELATIVE_FILE_PATH

```

# auth

simple auth wrapper using [firebase-admin-python](https://github.com/firebase/firebase-admin-python), where a user asked to input email along with mac address as identifier, then admin can approve users from firebase authentication.
