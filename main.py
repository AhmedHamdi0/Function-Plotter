import sys
import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from toolbar import Toolbar
from function_plotter import FunctionPlotter


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.setWindowTitle("Function Plotter")
        self.setGeometry(350, 200, 600, 500)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        self.toolbar = Toolbar(self)
        self.function_plotter = FunctionPlotter(self)

        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.function_plotter)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.main_layout.addWidget(self.canvas)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
