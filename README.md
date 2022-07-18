# Folder Structure
inspired by the mix of MVC (Model-View-Controller) pattern and DDD (Domain-driven design) pattern.

---
## <b>gui</b>
## <b>modules</b>
## <b>utils</b>


## <b>encrypt data</b>
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
    py -m utils.crypt -e file_path=RELATIVE_FILE_PATH

decrypt file with given filepath:
    py -m utils.crypt -d file_path=RELATIVE_FILE_PATH

```

# TODO
- ADD AUTH
- ADD SETTING/DATA JSON
- FIREBASE AUTH
- FINISH AUTOMATION
- ADD CRYPT HELPER

# THINGS TO IMPROVE
- BETTER DOCSTRING
- DECOUPLING
-