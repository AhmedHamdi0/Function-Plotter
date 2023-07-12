from PySide2.QtWidgets import QWidget


class FunctionPlotter(QWidget):
    def __init__(self, parent):
        super(FunctionPlotter, self).__init__(parent)
        self.function_input = None
        self.min_input = None
        self.max_input = None
        self.plot_button = None

        self.init_plotter()

    def init_plotter(self):
        print("Function Plotter")
