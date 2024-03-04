from PyQt6.QtWidgets import QMainWindow
from Window import Ui_MainWindow
import Model
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog

class MainWindow(QMainWindow):

    competition = None


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.hide()
        self.ui.Create.clicked.connect(self.createCompetition)
        self.ui.LoadCompetetion.clicked.connect(self.loadCompetetion)
        self.ui.UpdateCategory.clicked.connect(self.addCategory)
        
    def hideNewCompetitionLayout(self):
        self.ui.tabWidget.show()
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.CreateNewCompetetion.hide()
    
    def createCompetition(self):
        name = self.ui.CompetetionName.text()
        date = self.ui.CompetitionDate.text()
        if self.competition != None:
            self.competition.saveCompetition()
        self.competition = Model.Competition(name, date, [], [], [])
        self.hideNewCompetitionLayout()
        self.updateCompetetionUI()
        self.competition.saveCompetition()


    def updateCompetetionUI(self):
        self.ui.ChangeName.setText(self.competition.name)
        self.ui.ChangeDate.setText(self.competition.date)
        for category in self.competition.categories:
            self.ui.categories_2.addItem(category.__str__())
        for competitor in self.competition.competitors:
            self.ui.competitors_2.addItem(competitor.__str__())
        for table in self.competition.tables:
            self.ui.tables_2.addItem(table.__str__())

    def addCategory(self):
        age = self.ui.Age.text()
        weight = self.ui.Weight.text()
        hand = self.ui.Hand.text()
        gender = self.ui.Gender.text()
        self.competition.categories.append(Model.Category(age, weight, hand, gender, [], [], []))
        self.ui.categories_2.addItem(self.competition.categories[-1].__str__())
        self.competition.saveCompetition()


    def loadCompetetion(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        self.competition = Model.Competition.loadCompetition(fname[0])
        self.hideNewCompetitionLayout()
        self.updateCompetetionUI()
        

    def addCompetitor(self):
        pass

    def saveCompetetion(self):
        pass


