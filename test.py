import sys
import requests
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from backend.endpoints.employees import get_employees_list  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Dashboard with PyQtGraph")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        self.populate_employees_table()

        self.plot_data()

    def populate_employees_table(self):
        # Fetch data from API
        employees_data = get_employees_list()
        self.employees_data = employees_data

    def plot_data(self):
        # Example plotting: Number of employees in each role
        roles = {}
        for employee in self.employees_data:
            role = employee['role']
            if role in roles:
                roles[role] += 1
            else:
                roles[role] = 1

        roles_list = list(roles.keys())
        counts = list(roles.values())

        bar_graph = pg.BarGraphItem(x=list(range(len(roles_list))), height=counts, width=0.6, brush='r')
        self.plot_widget.addItem(bar_graph)
        self.plot_widget.getPlotItem().getAxis('bottom').setTicks([list(enumerate(roles_list))])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
