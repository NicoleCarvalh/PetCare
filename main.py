from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from pages.login_page import LoginPage
import sys

#TODO CRIAR / INSERIR LOADER AO LOGAR

# Initialize App
if __name__ == "__main__":
  app = QApplication(sys.argv)

  widget = QtWidgets.QStackedWidget()

  window = LoginPage(widget)

  widget.addWidget(window)
  # widget.setFixedHeight(1000)
  # widget.setFixedWidth(1600)
  widget.resize(1600, 950)
  widget.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))
  widget.setWindowTitle("PetCare Connect")
  widget.show()
  sys.exit(app.exec_())