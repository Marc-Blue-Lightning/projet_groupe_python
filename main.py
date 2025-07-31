import sys
from PySide6.QtWidgets import QApplication
from views.login_view import LoginWindow
from controllers.fist_admin import create_admin_user

#initilisation du premier utilisateur
create_admin_user()#ne s'execute qu'une seule fois par usage

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())
