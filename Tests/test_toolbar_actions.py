import pytest
from PySide2.QtWidgets import QFileDialog, QWidget, QMainWindow
from matplotlib import pyplot as plt

from widgets_actions import *


class MainWindowMock(QWidget):
    def __init__(self):
        super().__init__()
        self.figure = plt.figure()
        self.canvas = self.figure.canvas
        self.is_closed = False

    def close(self):
        self.is_closed = True


@pytest.fixture
def app(qtbot):
    """Create and return a GUI instance."""
    app = MainWindowMock()
    qtbot.addWidget(app)
    return app


def test_save_image(app, mocker):
    """Test case for the save_image function"""
    # Set up the custom mock for QFileDialog
    mocker.patch.object(
        QFileDialog,
        "getSaveFileName",
        return_value=("test_image.png", "PNG Files (*.png)"),
    )

    # Patch the figure's savefig method with a mock
    mocker.patch.object(app.figure, "savefig")

    # Call the save_image function
    save_image(app)

    # Verify that main_window.figure.savefig is called with the correct file name
    app.figure.savefig.assert_called_once_with("test_image.png")


def test_export_pdf(app, mocker):
    """Test case for the export_pdf function"""
    # Set up the custom mock for QFileDialog
    mocker.patch.object(
        QFileDialog,
        "getSaveFileName",
        return_value=("test_plot.pdf", "PDF Files (*.pdf)"),
    )

    # Patch the figure's savefig method with a mock
    mocker.patch.object(app.figure, "savefig")

    # Call the export_pdf function
    export_pdf(app)

    # Verify that main_window.figure.savefig is called with the correct file name and format
    app.figure.savefig.assert_called_once_with("test_plot.pdf", format='pdf')


def test_zoom_in(app):
    """Test case for the zoom_in function"""
    # Set initial x-axis and y-axis limits
    app.figure.gca().set_xlim(0, 10)
    app.figure.gca().set_ylim(0, 10)

    # Call the zoom_in function
    zoom_in(app)

    # Check if x-axis and y-axis limits are decreased by 10%
    assert app.figure.gca().get_xlim() == (0, 9)
    assert app.figure.gca().get_ylim() == (0, 9)


def test_zoom_out(app):
    """Test case for the zoom_out function"""
    # Set initial x-axis and y-axis limits
    app.figure.gca().set_xlim(0, 10)
    app.figure.gca().set_ylim(0, 10)

    # Call the zoom_out function
    zoom_out(app)

    # Check if x-axis and y-axis limits are increased by 10%
    assert app.figure.gca().get_xlim() == (0, 11)
    assert app.figure.gca().get_ylim() == (0, 11)


def test_exit_application(app):
    """Test case for the exit_application function"""
    # Call the exit_application function
    exit_application(app)

    # Check if the main window is closed
    assert app.is_closed

