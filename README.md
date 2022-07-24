# Folder Structure
inspired by the mix of MVC (Model-View-Controller) pattern and DDD (Domain-driven design) pattern.

---
## <b>gui</b>
## <b>modules</b>
## <b>utils</b>

---
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
    py -m utils.crypt -e -file_path=RELATIVE_FILE_PATH

decrypt file with given filepath:
    py -m utils.crypt -d -file_path=RELATIVE_FILE_PATH

```
# auth
simple auth wrapper using [firebase-admin-python](https://github.com/firebase/firebase-admin-python), where a user asked to input email along with mac address as identifier, then admin can approve users from firebase authentication.


# TODO
- ADD POPUP ANIMATION WHILE INPUT PROCESS TO EXCEL
- 
- FINISH AUTOMATION

# THINGS TO IMPROVE
- BETTER DOCSTRING
- DECOUPLING
-