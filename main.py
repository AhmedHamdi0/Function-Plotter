import sys
import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from toolbar import Toolbar
from function_plotter import FunctionPlotter
from widgets_actions import WidgetActions


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.setWindowTitle("Function Plotter")
        self.setGeometry(350, 200, 600, 500)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        self.widget_actions = WidgetActions(self)

        self.toolbar = Toolbar(self)
        self.function_plotter = FunctionPlotter(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_button = QPushButton("Plot", self)

        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.function_plotter)
        self.main_layout.addWidget(self.canvas)
        self.main_layout.addWidget(self.plot_button)

        self.plot_button.clicked.connect(self.widget_actions.plot)
        self.toolbar.new_plot_action.triggered.connect(self.widget_actions.new_plot)
        self.toolbar.add_subplot_action.triggered.connect(self.widget_actions.add_subplot)
        self.toolbar.save_image_action.triggered.connect(self.widget_actions.save_image)
        self.toolbar.export_pdf_action.triggered.connect(self.widget_actions.export_pdf)
        self.toolbar.zoom_in_action.triggered.connect(self.widget_actions.zoom_in)
        self.toolbar.zoom_out_action.triggered.connect(self.widget_actions.zoom_out)
        self.toolbar.exit_action.triggered.connect(self.widget_actions.exit_application)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
