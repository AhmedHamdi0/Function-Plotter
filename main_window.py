import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from toolbar import Toolbar
from function_plotter import FunctionPlotter
from widgets_actions import *


# Define the main application window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the application theme to dark using QDarkStyle
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        # Set window properties
        self.setWindowTitle("Function Plotter")
        self.setGeometry(350, 200, 600, 500)

        # Create the main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Create instances of the different components
        self.toolbar = Toolbar(self)
        self.function_plotter = FunctionPlotter(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_button = QPushButton("Plot", self)

        # Add the components to the main layout
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.function_plotter)
        self.main_layout.addWidget(self.canvas)
        self.main_layout.addWidget(self.plot_button)

        # Connect signals to slots for handling actions
        self.plot_button.clicked.connect(self.on_plot_button_clicked)
        self.toolbar.new_plot_action.triggered.connect(self.on_new_plot_action_triggered)
        self.toolbar.add_subplot_action.triggered.connect(self.on_add_subplot_action_triggered)
        self.toolbar.save_image_action.triggered.connect(lambda: save_image(self))
        self.toolbar.export_pdf_action.triggered.connect(lambda: export_pdf(self))
        self.toolbar.zoom_in_action.triggered.connect(lambda: zoom_in(self))
        self.toolbar.zoom_out_action.triggered.connect(lambda: zoom_out(self))
        self.toolbar.exit_action.triggered.connect(lambda: exit_application(self))

    def on_plot_button_clicked(self):
        function_str = self.function_plotter.function_input.text()
        min_value_str = self.function_plotter.min_input.text()
        max_value_str = self.function_plotter.max_input.text()
        plot(self, function_str, min_value_str, max_value_str)

    def on_new_plot_action_triggered(self):
        new_plot(self)

    def on_add_subplot_action_triggered(self):
        function_str = self.function_plotter.function_input.text()
        min_value_str = self.function_plotter.min_input.text()
        max_value_str = self.function_plotter.max_input.text()
        add_subplot(self, function_str, min_value_str, max_value_str)
