import pytest
from PySide2.QtWidgets import QMainWindow, QWidget
from toolbar import Toolbar


class MainWindowMock(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = QMainWindow()


@pytest.fixture
def app(qtbot):
    """Create and return a GUI instance."""
    app = MainWindowMock()
    qtbot.addWidget(app)
    return app


def test_toolbar_not_empty(app):
    """Test if the toolbar is not empty after initialization."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the toolbar is not empty
    assert toolbar.actions()


def test_new_plot_widget(app):
    """Test the 'New Plot' icon in the toolbar"""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.new_plot_action
    assert toolbar.new_plot_action.icon().isNull() is False
    assert toolbar.new_plot_action.text() == "New Plot"
    assert toolbar.new_plot_action.isCheckable() is True


def test_add_subplot_action(app):
    """Test the 'Add Subplot' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.add_subplot_action
    assert toolbar.add_subplot_action.icon().isNull() is False
    assert toolbar.add_subplot_action.text() == "Add Subplot"
    assert toolbar.add_subplot_action.isCheckable() is True


def test_save_image_action(app):
    """Test the 'Save Image' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.save_image_action
    assert toolbar.save_image_action.icon().isNull() is False
    assert toolbar.save_image_action.text() == "Save Image"
    assert toolbar.save_image_action.isCheckable() is True


def test_export_pdf_action(app):
    """Test the 'Export PDF' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.export_pdf_action
    assert toolbar.export_pdf_action.icon().isNull() is False
    assert toolbar.export_pdf_action.text() == "Export PDF"
    assert toolbar.export_pdf_action.isCheckable() is True


def test_zoom_in_action(app):
    """Test the 'Zoom In' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.zoom_in_action
    assert toolbar.zoom_in_action.icon().isNull() is False
    assert toolbar.zoom_in_action.text() == "Zoom In"
    assert toolbar.zoom_in_action.isCheckable() is True


def test_zoom_out_action(app):
    """Test the 'Zoom Out' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.zoom_out_action
    assert toolbar.zoom_out_action.icon().isNull() is False
    assert toolbar.zoom_out_action.text() == "Zoom Out"
    assert toolbar.zoom_out_action.isCheckable() is True


def test_exit_action(app):
    """Test the 'Exit App' icon in the toolbar."""
    # Create the toolbar instance
    toolbar = Toolbar(app)

    # Check if the action is created and has the correct icon, label, and is checkable
    assert toolbar.exit_action
    assert toolbar.exit_action.icon().isNull() is False
    assert toolbar.exit_action.text() == "Exit App"
    assert toolbar.exit_action.isCheckable() is True
