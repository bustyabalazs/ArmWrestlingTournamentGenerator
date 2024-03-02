# dialog.py

"""Dialog-style application."""

import sys
from Controller import MainWindow 

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit,
    QVBoxLayout, QToolBar, QStatusBar, QMainWindow, QLabel, QCheckBox,
    QMenu, QHBoxLayout, QPushButton, QWidget

)

#class CategoryWindow(QWidget):
    
    # def __init__(self):
    #     super().__init__()
    #     layout = QVBoxLayout()
    #     self.label = QLabel("Another Window")
    #     layout.addWidget(self.label)
    #     self.setLayout(layout)





if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())