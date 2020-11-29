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

        # Set default options
        self.createNewTableRB.setChecked(True)

    def get_options(self):
        """
        Converts checkboxes, radio buttons & entry fields into command line
        arguments.
        :return: a string of command line flags.
        """

        flags = ""

        # Creation options
        if self.createNewTableRB.isChecked():
            flags += '-c '
        elif self.appendToNewTableRB.isChecked():
            flags += '-a '
        elif self.recreateTableRB.isChecked():
            flags += '-d '
        elif self.createTableOnlyRB.isChecked():
            flags += '-p '

        # Constraint options
        if self.applyConstaintsCheckBox.isChecked():
            flags += '-C '
        if self.disableMaxExtentConstaintCheckBox.isChecked():
            flags += '-x '
        if self.setConstraintsBlockingCheckBox.isChecked():
            flags += '-r '

        # Raster processing options
        if self.setSRIDCheckBox.isChecked():
            input_srid = self.SRIDInput.text()
            if input_srid:
                flags += f"-s {input_srid} "
            else:
                print("Error: Missing SRID.")  #TODO: Popup window
        if self.extractBandCheckBox.isChecked():
            input_bands = self.extractBandInput.text()
            if input_bands:
                flags += f"-b {input_bands} "
            else:
                print("Error: Missing input bands.")

        if self.tileSizeCheckBox.isChecked():
            input_tile_size = self.tileSizeInput.text()
            if input_tile_size:
                flags += f"-t {input_tile_size} "
            else:
                print("Error: Missing input tile size.")

        if self.padTilesCheckBox.isChecked():
            flags += '-P '

        if self.OOBRasterCheckBox.isChecked():
            flags += '-R '

        if self.createOverviewsCheckBox.isChecked():
            input_overviews = self.overviewInput.text()
            if input_overviews:
                flags += f"-l {input_overviews} "
            else:
                print("Error: Missing input overview levels.")

        if self.setNoDataCheckBox.isChecked():
            input_nodata_value = self.noDataValueInput.text()
            if input_nodata_value:
                flags += f"-N {input_nodata_value} "
            else:
                print("Error: Missing input nodata value.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
