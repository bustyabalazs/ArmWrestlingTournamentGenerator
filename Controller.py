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
        self.ui.Update.clicked.connect(self.addCompetitor)
        self.ui.saveCompetetion.clicked.connect(self.changeCompetetionName)
        self.ui.Remove_2.clicked.connect(self.removeCategory)
        self.ui.categories_2.itemSelectionChanged.connect(self.updateCategoryInputs)
        self.ui.Remove.clicked.connect(self.removeCompetitor)
        self.ui.competitors_2.itemSelectionChanged.connect(self.updateCompetitorInputs)
        self.ui.UpdateTable.clicked.connect(self.addTable)
        self.ui.Remove_3.clicked.connect(self.removeTable)
        self.ui.tables_2.itemSelectionChanged.connect(self.updateTableInputs)
        self.ui.UpdateCountry.clicked.connect(self.addCountry)
        self.ui.Remove_4.clicked.connect(self.removeCountry)
        self.ui.countriesList.itemSelectionChanged.connect(self.updateCountryInputs)
        

        
    def hideNewCompetitionLayout(self):
        self.ui.tabWidget.show()
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.CreateNewCompetetion.hide()
    

    def createCompetition(self):
        name = self.ui.CompetetionName.text()
        date = self.ui.CompetitionDate.text()
        if self.competition != None:
            self.competition.saveCompetition()
        self.competition = Model.Competition(name, name, date, [], [], [])
        self.hideNewCompetitionLayout()
        self.updateCompetetionUI()
        self.competition.saveCompetition()


    def updateCompetetionUI(self):
        self.ui.ChangeName.setText(self.competition.name)
        self.ui.ChangeDate.setText(self.competition.date)
        self.updateCategoryList()
        self.updateCompetitorList()
        self.updateTableList()


    def addCategory(self):
        age = self.ui.Age.text()
        weight = self.ui.Weight.text()
        hand = self.ui.Hand.text()
        gender = self.ui.Gender.text()
        category = Model.Category(age, weight, hand, gender, [], [])
        if category not in self.competition.categories:
            self.competition.addCategory(category)
            self.competition.saveCompetition()
            self.updateCategoryList()


    def removeCategory(self):
        index = self.ui.categories_2.currentRow()
        self.ui.categories_2.takeItem(index)
        self.competition.categories.pop(index)
        self.competition.saveCompetition()


    def updateCategoryList(self):
        self.ui.categories_2.clear()
        for category in self.competition.categories:
            self.ui.categories_2.addItem(category.toString())


    def updateCategoryInputs(self):
        index = self.ui.categories_2.currentRow()
        category = self.competition.categories[index]
        self.ui.Age.setText(category.age)
        self.ui.Weight.setText(category.weight)
        self.ui.Hand.setText(category.hand)
        self.ui.Gender.setText(category.gender)


    def addCompetitor(self):
        name = self.ui.Name_2.text()
        category = self.ui.Categories.text()
        country = self.ui.Country.text()
        email = self.ui.email.text()
        competitor = Model.Competitor(len(self.competition.competitors), name, category, country, email)
        if competitor not in self.competition.competitors:
            self.competition.addCompetitor(competitor)
            self.competition.saveCompetition()
            self.updateCompetitorList()


    def removeCompetitor(self):
        index = self.ui.competitors_2.currentRow()
        self.ui.competitors_2.takeItem(index)
        self.competition.competitors.pop(index)
        self.competition.saveCompetition()


    def updateCompetitorInputs(self):
        index = self.ui.competitors_2.currentRow()
        competitor = self.competition.competitors[index]
        self.ui.Name_2.setText(competitor.name)
        self.ui.Categories.setText(competitor.category)
        self.ui.Country.setText(competitor.country)
        self.ui.email.setText(competitor.email)


    def updateCompetitorList(self):
        self.ui.competitors_2.clear()
        for competitor in self.competition.competitors:
            self.ui.competitors_2.addItem(competitor.toString())
    

    def addTable(self):
        table = self.ui.Table.text()
        if table not in self.competition.tables:
            self.competition.addTable(table)
            self.competition.saveCompetition()
            self.updateTableList()


    def removeTable(self):
        index = self.ui.tables_2.currentRow()
        self.ui.tables_2.takeItem(index)
        self.competition.tables.pop(index)
        self.competition.saveCompetition()


    def updateTableInputs(self):
        index = self.ui.tables_2.currentRow()
        table = self.competition.tables[index]
        self.ui.Table.setText(table)

    
    def updateTableList(self):
        self.ui.tables_2.clear()
        for table in self.competition.tables:
            self.ui.tables_2.addItem(table)


    def addCountry(self):
        country = self.ui.countries_name.text()
        if country not in self.competition.countries:
            self.competition.addCountry(country)
            self.competition.saveCompetition()
            self.updateCountryList()


    def removeCountry(self):
        index = self.ui.countriesList.currentRow()
        self.ui.countriesList.takeItem(index)
        self.competition.countries.pop(index)
        self.competition.saveCompetition()


    def updateCountryInputs(self):
        index = self.ui.countriesList.currentRow()
        country = self.competition.countries[index]
        self.ui.countries_name.setText(country)


    def updateCountryList(self):
        self.ui.countriesList.clear()
        for country in self.competition.countries:
            self.ui.countriesList.addItem(country)
    

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
        

    def changeCompetetionName(self):
        self.competition.name = self.ui.ChangeName.text()
        self.competition.date = self.ui.ChangeDate.text()
        self.competition.saveCompetition()


