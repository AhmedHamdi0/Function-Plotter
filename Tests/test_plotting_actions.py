import pytest
from PySide2.QtWidgets import QWidget
from matplotlib import pyplot as plt
from widgets_actions import plot, add_subplot, new_plot


class MainWindowMock(QWidget):
    def __init__(self):
        super().__init__()
        self.figure = plt.figure()
        self.canvas = self.figure.canvas


@pytest.fixture
def app(qtbot):
    """Create and return a GUI instance."""
    app = MainWindowMock()
    qtbot.addWidget(app)
    return app


# Testing plot function
def test_plot_with_valid_input(app, mocker):
    """Test plot with valid inputs"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(True, ""))

    # Calling the plot function with valid inputs
    plot(main_window=app, function_str='x^2', min_value_str='0', max_value_str='10')

    # Check if there is exactly one axis in the figure
    assert len(app.figure.axes) == 1
    # Check if the axis contains lines (indicating the plot is drawn)
    assert app.figure.axes[0].lines


def test_plot_with_invalid_function_input(app, mocker):
    """Test plot with invalid input function"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid function. Please enter a valid mathematical function."))

    # Calling the plot function with invalid function input
    plot(main_window=app, function_str="some text", min_value_str='0', max_value_str='10')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_plot_with_invalid_min_input(app, mocker):
    """Test plot with invalid min input"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Please enter valid numbers."))

    # Calling the plot function with invalid input min value
    plot(main_window=app, function_str='x^2', min_value_str='abc', max_value_str='10')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_plot_invalid_max_input(app, mocker):
    """Test plot with invalid max input"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Please enter valid numbers."))

    # Calling the plot function with invalid input max value
    plot(main_window=app, function_str='x^2', min_value_str='2', max_value_str='abc')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_plot_with_min_greater_than_max(app, mocker):
    """Test plot with min greater than max"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Max value should be greater than min value."))

    # Calling the plot function with invalid input value (min > max)
    plot(main_window=app, function_str='x^2', min_value_str='5', max_value_str='1')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


# Testing add_subplot function
def test_add_subplot_with_valid_input(app, mocker):
    """Test plot with valid inputs"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(True, ""))

    # Calling the add_subplot function with valid input
    add_subplot(main_window=app, function_str='x^2', min_value_str='0', max_value_str='10')

    # Check if there is exactly one axis in the figure
    assert len(app.figure.axes) == 1
    # Check if the axis contains lines (indicating the plot is drawn)
    assert app.figure.axes[0].lines


def test_add_subplot_with_invalid_function_input(app, mocker):
    """Test plot with invalid input function"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid function. Please enter a valid mathematical function."))

    # Calling the add_subplot function with invalid input function
    add_subplot(main_window=app, function_str="some text", min_value_str='0', max_value_str='10')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_add_subplot_with_invalid_min_input(app, mocker):
    """Test plot with invalid min input"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Please enter valid numbers."))

    # Calling the add_subplot function with invalid input min value
    add_subplot(main_window=app, function_str='x^2', min_value_str='abc', max_value_str='10')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_add_subplot_invalid_max_input(app, mocker):
    """Test plot with invalid max input"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Please enter valid numbers."))

    # Calling the add_subplot function with invalid input max value
    add_subplot(main_window=app, function_str='x^2', min_value_str='2', max_value_str='abc')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


def test_add_subplot_with_min_greater_than_max(app, mocker):
    """Test plot with min greater than max"""
    # Mocking the validate_input function
    mocker.patch('widgets_actions.validate_input', return_value=(False, "Invalid min/max values. Max value should be greater than min value."))

    # Calling the add_subplot function with invalid input (min > max)
    add_subplot(main_window=app, function_str='x^2', min_value_str='5', max_value_str='1')

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes


# Testing new_plot function
def test_new_plot(app):
    """Test new plot function"""
    # Call the new_plot function
    new_plot(main_window=app)

    # Check if the figure is cleared and canvas is updated
    assert not app.figure.axes
