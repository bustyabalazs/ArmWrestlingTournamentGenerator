# dialog.py

"""Dialog-style application."""

import classes
import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit,
    QVBoxLayout, QToolBar, QStatusBar, QMainWindow, QLabel, QCheckBox,
    QMenu

)


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")

        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        newCompetetion_action = QAction("&new competition", self)
        loadCompetetion_action = QAction("&open competition from file", self)
        #button_action.setStatusTip("This is your button")
        newCompetetion_action.triggered.connect(self.createNewCompetetion)
        loadCompetetion_action.triggered.connect(self.loadCompetetionFromFile)
        #button_action.setCheckable(True)
        #button_action.setShortcut(QKeySequence("Ctrl+p"))
        #toolbar.addAction(button_action)

        toolbar.addSeparator()

        # button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        # button_action2.setStatusTip("This is your button2")
        # button_action2.triggered.connect(self.onMyToolBarButtonClick)
        # button_action2.setCheckable(True)
        # toolbar.addAction(button_action)

        # toolbar.addWidget(QLabel("Hello"))
        # toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        competition_menu = menu.addMenu("&Competition")
        competition_menu.addAction(newCompetetion_action)
        competition_menu.addAction(loadCompetetion_action)

        competition_menu.addSeparator()

        # file_submenu = file_menu.addMenu("Submenu")

        # file_submenu.addAction(button_action2)


    def createNewCompetetion(self):
        pass
    
    def loadCompetetionFromFile(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    #create_comptetion_window = CreateCompetitionWindow()
    w = MainWindow()
    w.show()
    sys.exit(app.exec())