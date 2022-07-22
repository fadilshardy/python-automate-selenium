import os
import firebase_admin

from firebase_admin import credentials
from utils import crypt
from utils import path

def initialize_firebase():
    """
    initiate firebase admin instance
    """
    try:
        encrypted_firebase_sdk = os.path.join(path.get_resource_path(), 'firebase-sdk.json')

        key = crypt.load_key()

        decrypted_firebase_sdk = crypt.decrypt_to_dict(encrypted_firebase_sdk, key)

        cred = credentials.Certificate(decrypted_firebase_sdk)

        app = firebase_admin.initialize_app(cred)

        return app
    except Exception as e:
        print(e)
