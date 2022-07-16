import firebase_admin
from firebase_admin import credentials
from resource.crypt import load_key, decrypt, to_dict


def initialize_firebase():
    try:
        credential_path = r'resource\sdk.bin'

        key = load_key()

        decrypt_credentials = decrypt(credential_path, key)

        credential = to_dict(decrypt_credentials)

        cred = credentials.Certificate(credential)

        app = firebase_admin.initialize_app(cred)

        return app
    except Exception as e:
        print(e)
