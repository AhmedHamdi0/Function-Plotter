import sys
from main_window import MainWindow
from PySide2.QtWidgets import QApplication
from styles import stylesheet

if __name__ == '__main__':
    # Initialize and run the Qt application with the main window
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
