import sys
import qdarkstyle
from PySide2.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.setWindowTitle("Function Plotter")
        self.setGeometry(350, 200, 600, 500)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
