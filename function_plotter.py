from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


# Define a custom QWidget class for the function plotter
class FunctionPlotter(QWidget):
    def __init__(self, parent):
        super(FunctionPlotter, self).__init__(parent)

        # Initialize input fields for function, min value of x, and max value of x
        self.function_input = None
        self.min_input = None
        self.max_input = None

        # Set up the function plotter
        self.init_plotter()

    def init_plotter(self):
        # Create a vertical layout for the plotter widget
        plotter_layout = QVBoxLayout(self)

        # Create a horizontal layout for the function input field
        function_layout = QHBoxLayout()

        function_label = QLabel("Enter function (e.g., 5*x^3 + 2*x):", self)
        self.function_input = QLineEdit(self)

        function_layout.addWidget(function_label)
        function_layout.addWidget(self.function_input)

        # Create a horizontal layout for the min and max value of x input fields
        value_x_layout = QHBoxLayout()

        min_label = QLabel("Enter min value of x:", self)
        self.min_input = QLineEdit(self)
        max_label = QLabel("Enter max value of x:", self)
        self.max_input = QLineEdit(self)

        value_x_layout.addWidget(min_label)
        value_x_layout.addWidget(self.min_input)
        value_x_layout.addWidget(max_label)
        value_x_layout.addWidget(self.max_input)

        # Add the function and value of x layouts to the plotter layout
        plotter_layout.addLayout(function_layout)
        plotter_layout.addLayout(value_x_layout)
