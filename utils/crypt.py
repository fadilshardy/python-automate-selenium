import os
import ast #noqa

from cryptography.fernet import Fernet

from utils import path


def generate_crypt_key():
    """
    Generates a key and save it inside resource directory as `crypt.key`
    """

    key_path = os.path.join(path.get_resource_path(), 'crypt.key')

    os.makedirs(os.path.dirname(key_path), exist_ok=True)

    crypt_key = Fernet.generate_key()

    with open(key_path, "wb") as key_file:
        key_file.write(crypt_key)


def load_key():
    """
    Loads the key from the resource directory named `crypt.key`
    """
    key_path = os.path.join(path.get_resource_path(), 'crypt.key')

    return open(key_path, "rb").read()


def encrypt_file(filename, crypt_key):
    """
    encrypts the file and write it
    """

    fernet = Fernet(crypt_key)

    with open(filename, "rb") as file_tempt:
        file_data = file_tempt.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename, "wb") as file_tempt:
        file_tempt.write(encrypted_data)


def decrypt_file(filename, crypt_key):
    """
    decrypts the file and write it
    """

    fernet = Fernet(crypt_key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)


def decrypt_to_bytes(filename, crypt_key) -> bytes:
    """
    decrypts the file

    :return: decrypted data bytes
    """

    fernet = Fernet(crypt_key)
    with open(filename, "rb") as file_tempt:
        encrypted_data = file_tempt.read()

    decrypted_data_bytes = fernet.decrypt(encrypted_data)

    decrypted_data = decrypted_data_bytes.decode("UTF-8")

    return decrypted_data

def decrypt_to_dict(filename, crypt_key) -> dict:
    """
    decrypts file to dictionaries type

    :return: decypted data (dict)
    """

    decrypted_data_bytes = decrypt_to_bytes(filename, crypt_key)

    decrypted_data_dict = convert_to_dict(decrypted_data_bytes)

    return decrypted_data_dict




def convert_to_dict(data) -> dict:
    """
    convert given data to dict

    :return: dict data
    """

    converted_data = ast.literal_eval(data)

    return converted_data


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Simple File Encryptor Script")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")
    parser.add_argument("-file_path",
                        help="File path to encrypt/decrypt")

    args = parser.parse_args()
    generate_key = args.generate_key
    encrypt_ = args.encrypt
    decrypt_ = args.decrypt
    file_path = args.file_path

    if generate_key:
        generate_crypt_key()
        print('key generated')

    key = load_key()

    if encrypt_ and not args.file_path:
        parser.error('-file_path is required when --encrypt is set.')
    elif encrypt_ and decrypt_:
        raise TypeError(
            "Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt_file(file_path, key)
        print('file encrypted')
    elif decrypt_:
        decrypt_file(file_path, key)
        print('file decrypted')
