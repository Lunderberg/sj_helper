#!/usr/bin/env python3

import os
import sys

from PyQt4 import uic, QtGui, QtCore

readout_base = '/user/lunderbe/DDAS/readout11'
set_files = {
    'notrace_novalidate':[
        ('crate_1/crate_1.set',   'crate_1/2016-01-20_NoTrace_NoValidate.set'),
        ('crate_1/modevtlen.txt', 'crate_1/notrace_modevtlen.txt'),
        ('crate_2/crate_2.set',   'crate_2/2016-01-20_NoTrace_NoValidate.set'),
        ('crate_2/modevtlen.txt', 'crate_2/notrace_modevtlen.txt'),
        ('crate_3/crate_3.set',   'crate_3/2016-01-20_NoTrace_NoValidate.set'),
        ('crate_3/modevtlen.txt', 'crate_3/notrace_modevtlen.txt'),
        ],
    'withtrace_withvalidate':[
        ('crate_1/crate_1.set',   'crate_1/2016-01-20_WithTrace_WithValidate.set'),
        ('crate_1/modevtlen.txt', 'crate_1/withtrace_modevtlen.txt'),
        ('crate_2/crate_2.set',   'crate_2/2016-01-20_WithTrace_WithValidate.set'),
        ('crate_2/modevtlen.txt', 'crate_2/withtrace_modevtlen.txt'),
        ('crate_3/crate_3.set',   'crate_3/2016-01-20_WithTrace_WithValidate.set'),
        ('crate_3/modevtlen.txt', 'crate_3/withtrace_modevtlen.txt'),
        ],
    }

# Prepend the readout_base to all paths
set_files = {
    category:[
        (os.path.join(readout_base,dest),os.path.join(readout_base,src))
        for dest,src in symlinks
    ]
    for category,symlinks in set_files.items()
}

# Load the GUI class from the .ui file
script_dir = os.path.dirname(__file__)
(Ui_MainWindow, QMainWindow) = uic.loadUiType(os.path.join(script_dir,'GUI_design.ui'))

# Define a class for the main window.
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Initialize the GUI itself
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect a function to be run when a button is pressed.
        self.ui.notraces_novalidation.clicked.connect(self.NoTraces_NoValidation)
        self.ui.withtraces_withvalidation.clicked.connect(self.WithTraces_WithValidation)

    def NoTraces_NoValidation(self,*args):
        make_symlinks(set_files['notrace_novalidate'])

    def WithTraces_WithValidation(self,*args):
        make_symlinks(set_files['withtrace_withvalidate'])


def make_symlinks(symlinks):
    should_stop = False
    for dest, src in symlinks:
        # Input path exists
        if not os.path.exists(src):
            print('{} does not exist'.format(src))
            should_stop = True

        # Output folder exists
        dirname = os.path.dirname(dest)
        if not os.path.exists(dirname):
            print('{} does not exist'.format(dirname))
            should_stop = True

        # Output path exists and is not a symlink
        if os.path.exists(dest) and not os.path.islink(dest):
            print('{} already exists, and is not a symlink'.format(dest))
            should_stop = True


    if should_stop:
        return

    for dest, src in symlinks:
        if os.path.exists(dest):
            os.unlink(dest)
        os.symlink(src, dest)

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
