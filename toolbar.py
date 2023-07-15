from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QToolBar, QAction


# Define a custom toolbar class
class Toolbar(QToolBar):
    def __init__(self, parent):
        super(Toolbar, self).__init__(parent)

        # Initialize toolbar actions
        self.new_plot_action = None
        self.add_subplot_action = None
        self.save_image_action = None
        self.export_pdf_action = None
        self.zoom_in_action = None
        self.zoom_out_action = None
        self.exit_action = None

        # Set up the toolbar
        self.init_toolbar()

    # Set up the toolbar
    def init_toolbar(self):
        # Create and configure actions with icons and labels
        self.new_plot_action = QAction(QIcon("Assets/function.png"), "New Plot", self)
        self.new_plot_action.setCheckable(True)

        self.add_subplot_action = QAction(QIcon("Assets/blueprint--plus.png"), "Add Subplot", self)
        self.add_subplot_action.setCheckable(True)

        self.save_image_action = QAction(QIcon("Assets/document-image.png"), "Save Image", self)
        self.save_image_action.setCheckable(True)

        self.export_pdf_action = QAction(QIcon("Assets/blue-document-pdf-text.png"), "Export PDF", self)
        self.export_pdf_action.setCheckable(True)

        self.zoom_in_action = QAction(QIcon("Assets/magnifier-zoom-in.png"), "Zoom In", self)
        self.zoom_in_action.setCheckable(True)

        self.zoom_out_action = QAction(QIcon("Assets/magnifier-zoom-out.png"), "Zoom Out", self)
        self.zoom_out_action.setCheckable(True)

        self.exit_action = QAction(QIcon("Assets/cross-script.png"), "Exit App", self)
        self.exit_action.setCheckable(True)

        # Add actions to the toolbar
        self.addAction(self.new_plot_action)
        self.addAction(self.add_subplot_action)
        self.addAction(self.save_image_action)
        self.addAction(self.export_pdf_action)
        self.addAction(self.zoom_in_action)
        self.addAction(self.zoom_out_action)
        self.addAction(self.exit_action)
