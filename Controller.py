from PyQt6.QtWidgets import QMainWindow
from Window import Ui_MainWindow
import Model

class MainWindow(QMainWindow):
    competition = None
    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.UpdateCategory.clicked.connect(self.addCategory)
    
    def addCategory(self):
        age = self.ui.Age.text()
        weight = self.ui.Weight.text()
        hand = self.ui.Hand.text()
        gender = self.ui.Gender.text()
        self.competition.categories.append(Model.Category(age, weight, hand, gender))
        self.ui.categories_2.addItem(self.competition.categories[-1].__str__())


    def addCompetitor(self):
        pass


