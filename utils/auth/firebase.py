from firebase_admin import auth
from getmac import get_mac_address as gma

from utils.auth.initialize_admin import initialize_firebase


class Firebase():
    """
    Represents main Firebase class instance.
    """
    def __init__(self):
        self.app = initialize_firebase()
        self.user_mac_address = gma()

    def register_user(self, email):
        """
        register a user to firebase authentication using mac address as uid
        """
        try:
            auth.create_user(
                email=email, uid=self.user_mac_address, disabled=True)
        except Exception as error:
            print(error)

    def check_user(self) -> str:
        """
        check if user is active

        :return: user status (str)
        """

        try:
            user = auth.get_user(self.user_mac_address)
        except auth.UserNotFoundError:
            return "notRegistered"
        except Exception:
            return "connectionError"

        if user.disabled is not True:
            return "active"

        if user.disabled is True :
            return "notActive"

        return "unknown"

    def get_user_email(self) -> str:
        """
        get user email by mac address

        :return: user email
        """
        user = auth.get_user(self.user_mac_address)

        email = user.email

        return email
