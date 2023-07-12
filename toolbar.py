from PySide2.QtWidgets import QToolBar


class Toolbar(QToolBar):
    def __init__(self, parent):
        super(Toolbar, self).__init__(parent)
        self.new_plot_action = None
        self.add_subplot_action = None
        self.save_image_action = None
        self.export_pdf_action = None
        self.zoom_in_action = None
        self.zoom_out_action = None
        self.exit_action = None

        self.init_toolbar()

    def init_toolbar(self):
        print("Toolbar")
