from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class FunctionPlotter(QWidget):
    def __init__(self, parent):
        super(FunctionPlotter, self).__init__(parent)
        self.function_input = None
        self.min_input = None
        self.max_input = None
        self.plot_button = None

        self.init_plotter()

    def init_plotter(self):
        plotter_layout = QVBoxLayout()

        function_layout = QHBoxLayout()
        function_label = QLabel("Enter function (e.g., 5*x^3 + 2*x):", self)
        self.function_input = QLineEdit(self)

        function_layout.addWidget(function_label)
        function_layout.addWidget(self.function_input)

        value_x_layout = QHBoxLayout()
        min_label = QLabel("Enter min value of x:", self)
        self.min_input = QLineEdit(self)
        max_label = QLabel("Enter max value of x:", self)
        self.max_input = QLineEdit(self)

        value_x_layout.addWidget(min_label)
        value_x_layout.addWidget(self.min_input)
        value_x_layout.addWidget(max_label)
        value_x_layout.addWidget(self.max_input)

        self.plot_button = QPushButton("Plot", self)

        plotter_layout.addLayout(function_layout)
        plotter_layout.addLayout(value_x_layout)
        plotter_layout.addWidget(self.plot_button)

