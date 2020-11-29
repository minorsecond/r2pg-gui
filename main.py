import sys
from gui.mainwindow import QtWidgets, Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Main window class.
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
