# dialog.py

"""Dialog-style application."""

import classes
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class CreateCompetitionWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Competition")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Date:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)
        self.btn_ok.clicked.connect(self.accept)
        self.show()


    
    def accept(self):
        """Accept and close the dialog."""
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    create_comptetion_window = CreateCompetitionWindow()
    sys.exit(app.exec())