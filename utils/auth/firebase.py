from firebase_admin import auth
from firebase_admin import exceptions

from getmac import get_mac_address as gma

from auth.initialize_admin import initialize_firebase


class Firebase():
    def __init__(self):
        self.app = initialize_firebase()
        self.user_mac_address = gma()

    def create_user(self, email):
        try:
            auth.create_user(
                email=email, uid=self.user_mac_address, disabled=True)
        except Exception as e:
            print(e)

    def check_user(self):

        try:
            # check by uid (mac address)
            user = auth.get_user(self.user_mac_address)
        except auth.UserNotFoundError:
            return "notRegistered"
        except Exception:
            return "connectionError"

            # check if user is active
        if(user.disabled != True):
            return "active"
        elif(user.disabled == True):
            return "fas"
        else:
            return "unknown"

    def get_user_email(self):
        user = auth.get_user(self.user_mac_address)

        email = user.email

        return email
