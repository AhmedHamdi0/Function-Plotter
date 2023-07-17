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


# To plot a mathematical function on a canvas using matplotlib
def plot(main_window, function_str, min_value_str, max_value_str):
    function_str = function_str.replace('^', '**')  # Replace ^ with ** for exponentiation
    valid_input, error_message = validate_input(function_str, min_value_str, max_value_str)

    if valid_input:
        x = np.linspace(float(min_value_str), float(max_value_str), 1000)
        y = eval(function_str)

        main_window.figure.clear()
        ax = main_window.figure.add_subplot(111)
        ax.plot(x, y)
        main_window.canvas.draw()
    else:
        QMessageBox.critical(main_window, "Invalid Input", error_message, QMessageBox.Ok)


# Clear the existing figure and prepare for a new plot
def new_plot(main_window):
    main_window.figure.clear()
    main_window.canvas.draw()


# To add subplot on the canvas without erasing the previous plot
def add_subplot(main_window, function_str, min_value_str, max_value_str):
    function_str = function_str.replace('^', '**')  # Replace ^ with ** for exponentiation
    valid_input, error_message = validate_input(function_str, min_value_str, max_value_str)

    if valid_input:
        x = np.linspace(float(min_value_str), float(max_value_str), 1000)
        y = eval(function_str)

        ax = main_window.figure.gca()
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
        color = random.choice(colors)
        ax.plot(x, y, color=color)
        main_window.canvas.draw()
    else:
        QMessageBox.critical(main_window, "Invalid Input", error_message, QMessageBox.Ok)


# Save the plot as an image file with the chosen file name
def save_image(main_window):
    default_dir = expanduser("~/Downloads")
    file_name, _ = QFileDialog.getSaveFileName(main_window, "Save Image", default_dir,
                                               "PNG Files (*.png);;All Files (*)")

    if file_name:
        main_window.figure.savefig(file_name)


# Export the plot as a PDF file with the chosen file name
def export_pdf(main_window):
    default_dir = expanduser("~/Downloads")
    file_name, _ = QFileDialog.getSaveFileName(main_window, "Export PDF", default_dir,
                                               "PDF Files (*.pdf);;All Files (*)")

    if file_name:
        main_window.figure.savefig(file_name, format='pdf')


# Zoom in of the plot by decreasing the x-axis and y-axis limits.
def zoom_in(main_window):
    ax = main_window.figure.gca()
    ax.set_xlim(0.9 * ax.get_xlim()[0], 0.9 * ax.get_xlim()[1])
    ax.set_ylim(0.9 * ax.get_ylim()[0], 0.9 * ax.get_ylim()[1])
    main_window.canvas.draw()


# Zoom out of the plot by increasing the x-axis and y-axis limits.
def zoom_out(main_window):
    ax = main_window.figure.gca()
    ax.set_xlim(1.1 * ax.get_xlim()[0], 1.1 * ax.get_xlim()[1])
    ax.set_ylim(1.1 * ax.get_ylim()[0], 1.1 * ax.get_ylim()[1])
    main_window.canvas.draw()


# Exit the application
def exit_application(main_window):
    main_window.close()
