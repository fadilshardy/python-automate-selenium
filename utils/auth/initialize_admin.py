import firebase_admin
from firebase_admin import credentials
from utils import crypt


def initialize_firebase():
    """
    initiate firebase admin instance
    """
    try:
        firebase_sdk = r'resource\firebase-sdk.json'

        key = crypt.load_key()

        decrypt_sdk = crypt.decrypt_to_bytes(firebase_sdk, key)

        credential = crypt.convert_to_dict(decrypt_sdk)

        cred = credentials.Certificate(credential)

        app = firebase_admin.initialize_app(cred)

        return app
    except Exception as e:
        print(e)
