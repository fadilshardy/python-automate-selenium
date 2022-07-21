from dataclasses import dataclass

from firebase_admin import auth
from getmac import get_mac_address

from utils.auth.initialize_admin import initialize_firebase


@dataclass
class Firebase():
    """
    Represents main Firebase class instance.
    """
    try:
        app = initialize_firebase()
        user_mac_address = get_mac_address()
    except Exception as e:
        print(e)

    def register_user(self, email):
        """
        register a user to firebase authentication using mac address as uid
        """
        try:
            auth.create_user(
                email=email, uid=self.user_mac_address, disabled=True)
        except Exception as error:
            print(error)

    def check_user_status(self) -> str:
        """
        check if user is active

        :return: user status (str)
        """
        user = self.get_user()

        if user.disabled:
            return False

        if user.disabled is None:
            return None

        return True

    def get_user(self) -> object:
        """
        get user by uid (mac address)

        :return: user status (str)
        """

        try:
            return auth.get_user(self.user_mac_address)

        except auth.UserNotFoundError:
            return None
        except Exception as error:
            raise ValueError("Connection error") from error

    def get_user_email(self) -> str:
        """
        get user email by mac address

        :return: user email
        """
        user = auth.get_user(self.user_mac_address)

        email = user.email

        return email
