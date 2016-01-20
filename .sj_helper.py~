#!/usr/bin/env python3

import sys
from PyQt4 import uic, QtGui, QtCore

# Load the GUI class from the .ui file
(Ui_MainWindow, QMainWindow) = uic.loadUiType('example.ui')

# Define a class for the main window.
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Initialize the GUI itself
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect a function to be run when a button is pressed.
        self.ui.save.clicked.connect(self.from_SaveButtonClicked)

    # Here, defining a method.
    # qt passes in additional arguments that this function does not need,
    # so I use *args to ignore them.
    def from_SaveButtonClicked(self,*args):
        filetype = '.set'
        filename = str(QtGui.QFileDialog.getSaveFileName(self,'Save Settings File','',
                                                         'Settings file (*{})'.format(filetype)))

        # filename is empty string if user hits cancel, so don't save anything
        if filename:
            if not filename.endswith(filetype):
                filename += filetype
            self.SaveSettings(filename)

    def SaveSettings(self,filename):
        print('Saving',filename)

        # With statement automatically closes file at end.
        with open(filename,'w') as f:
            text_value = self.ui.text_entry.text()
            f.write('Text field: {}\n'.format(text_value))

            integer_value = self.ui.spin_integer.value()
            f.write('Integer field: {}\n'.format(integer_value))

            double_value = self.ui.spin_double.value()
            f.write('Double field: {}\n'.format(double_value))

            dropdown_index = self.ui.dropdown.currentIndex()
            dropdown_text = self.ui.dropdown.currentText()
            f.write('Dropdown: Index={}, Text={}\n'.format(dropdown_index,dropdown_text))


if __name__=='__main__':
    # Initialize the qt event loop.
    app = QtGui.QApplication(sys.argv)
    # Initialize and display our main window.
    w = MainWindow()
    w.show()
    # Run the qt event loop, exiting the script when done.
    sys.exit(app.exec_())
