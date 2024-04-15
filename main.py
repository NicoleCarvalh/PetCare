from PyQt5.QtWidgets import QApplication, QDialog, QFrame, QLabel, QLineEdit

from PyQt5 import uic

from PyQt5.QtGui import QIcon

import sys

class Main(QDialog):
  def __init__(self):
    super(Main, self).__init__()
    

    # Load the UI file
    uic.loadUi("screens/login.ui", self)
    
    self.setWindowTitle("PetCare Connect")
    self.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))


# Initialize App
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Main()
  window.show()
  app.exec_()


  

# from PyQt5.uic import loadUi

# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         loadUi("screens/login.ui", self)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()

###############################

# from PyQt5.QtUiTools import QUiLoader


# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__()

#         loader = QUiLoader()
#         self.ui = loader.load("screens/login.ui")
#         self.setCentralWidget(self.ui)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
