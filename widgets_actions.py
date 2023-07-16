from os.path import expanduser
import numpy as np
from PySide2.QtWidgets import QMessageBox, QFileDialog
from numpy import random


# Check input validation
def validate_input(function_str, min_value_str, max_value_str):
    # Check if the function is valid
    try:
        x = 0
        eval(function_str)
    except (SyntaxError, NameError, ZeroDivisionError):
        return False, "Invalid function. Please enter a valid mathematical function."

    # Check if min and max values are valid numbers
    try:
        min_value = float(min_value_str)
        max_value = float(max_value_str)
    except ValueError:
        return False, "Invalid min/max values. Please enter valid numbers."

    # Check if min_value is smaller than max_value
    if min_value >= max_value:
        return False, "Invalid min/max values. Max value should be greater than min value."

    return True, ""


# Define a class for handling widget actions
class WidgetActions:
    def __init__(self, parent):
        self.parent = parent

    # To plot a mathematical function on a canvas using matplotlib
    def plot(self):
        function_str = self.parent.function_plotter.function_input.text()
        function_str = function_str.replace('^', '**')  # Replace ^ with ** for exponentiation
        min_value_str = self.parent.function_plotter.min_input.text()
        max_value_str = self.parent.function_plotter.max_input.text()

        valid_input, error_message = validate_input(function_str, min_value_str, max_value_str)

        if valid_input:
            x = np.linspace(float(min_value_str), float(max_value_str), 1000)
            y = eval(function_str)

            self.parent.figure.clear()
            ax = self.parent.figure.add_subplot(111)
            ax.plot(x, y)
            self.parent.canvas.draw()
        else:
            QMessageBox.critical(self.parent, "Invalid Input", error_message, QMessageBox.Ok)

    # Clear the existing figure and prepare for a new plot
    def new_plot(self):
        self.parent.figure.clear()
        self.parent.canvas.draw()

    # To add subplot on the canvas without erasing the previous plot
    def add_subplot(self):
        function_str = self.parent.function_plotter.function_input.text()
        function_str = function_str.replace('^', '**')  # Replace ^ with ** for exponentiation
        min_value_str = self.parent.function_plotter.min_input.text()
        max_value_str = self.parent.function_plotter.max_input.text()

        valid_input, error_message = validate_input(function_str, min_value_str, max_value_str)

        if valid_input:
            x = np.linspace(float(min_value_str), float(max_value_str), 1000)
            y = eval(function_str)

            ax = self.parent.figure.gca()
            colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
            color = random.choice(colors)
            ax.plot(x, y, color=color)
            self.parent.canvas.draw()
        else:
            QMessageBox.critical(self.parent, "Invalid Input", error_message, QMessageBox.Ok)

    # Save the plot as an image file with the chosen file name
    def save_image(self):
        default_dir = expanduser("~/Documents")
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Save Image", default_dir,
                                                   "PNG Files (*.png);;All Files (*)")

        if file_name:
            self.parent.figure.savefig(file_name)

    # Export the plot as a PDF file with the chosen file name
    def export_pdf(self):
        default_dir = expanduser("~/Documents")
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Export PDF", default_dir,
                                                   "PDF Files (*.pdf);;All Files (*)")

        if file_name:
            self.parent.figure.savefig(file_name, format='pdf')

    # Zoom in of the plot by decreasing the x-axis and y-axis limits.
    def zoom_in(self):
        ax = self.parent.figure.gca()
        ax.set_xlim(0.9 * ax.get_xlim()[0], 0.9 * ax.get_xlim()[1])
        ax.set_ylim(0.9 * ax.get_ylim()[0], 0.9 * ax.get_ylim()[1])
        self.parent.canvas.draw()

    # Zoom out of the plot by increasing the x-axis and y-axis limits.
    def zoom_out(self):
        ax = self.parent.figure.gca()
        ax.set_xlim(1.1 * ax.get_xlim()[0], 1.1 * ax.get_xlim()[1])
        ax.set_ylim(1.1 * ax.get_ylim()[0], 1.1 * ax.get_ylim()[1])
        self.parent.canvas.draw()

    # Exit the application
    def exit_application(self):
        self.parent.close()
