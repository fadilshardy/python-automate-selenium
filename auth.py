
import route

from gui import popup
from gui.register_gui import RegisterGui
from utils.auth.firebase import Firebase


class Auth:
    """
    Auth class to handle logic related to authentication
    """

    firebase = Firebase()

    def open_register_gui(self):
        """
        open register gui instance
        """
        register_window = RegisterGui().start_gui()
        while True:
            try:
                event, values = register_window.read()

                route.register_event(
                    event, values, register_window, self.firebase)

                if event in ('Exit', 'WIN_CLOSED'):
                    register_window.close()
                    del register_window
                    break

            except Exception as e:
                print(e)

    def check(self):
        """
        auth guard based on user status
        """
        try:
            user = self.firebase.get_user()

            if user is None:
                self.open_register_gui()
                return None

            if user.disabled:
                error_message = f'Komputer ini sudah di register dengan email {user.email}, kontak admin untuk validasi akun.'
                popup.error_popup(error_message)
                return False

            if not user.disabled:
                return True

            return True
        except Exception as error:
            error_message = 'Terjadi kesalahan saat melakukan autentikasi ke database, cek koneksi internet.'
            popup.error_popup(error_message)
            print(error)
