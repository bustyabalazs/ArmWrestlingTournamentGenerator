from PyQt6.QtWidgets import QMainWindow
from Window import Ui_MainWindow
from CategoryView import Ui_CategoryView
import Model
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtWidgets import QLabel

class CategoryView(QMainWindow):
    def __init__(self, category, tables, competitors):
        super().__init__()
        self.ui = Ui_CategoryView()
        self.ui.setupUi(self)
        self.category = category
        self.category.bracket = Model.Bracket(competitors)
        self.tables = tables
        self.updateCategoryUI()
        self.ui.comboBox.currentIndexChanged.connect(self.updateTableSelection)

    def updateCategoryUI(self):
        self.category.bracket.genBracket()
        self.updateTableList()
        self.updateNextMatches()
        self.updateFinishedMatches()

    
    def generateBracket(self):
        
        self.updateNextMatches()
        self.updateFinishedMatches()

    def updateTableList(self):
        self.ui.comboBox.clear()
        for table in self.tables:
            if table.runningCategory is None:
                self.ui.comboBox.addItem(table.name)
            elif table.runningCategory == self.category:
                self.ui.comboBox.addItem(table.name)
    
    def updateNextMatches(self):
        self.ui.listWidget.clear()
        for match in self.category.bracket.next_matches:
            self.ui.listWidget.addItem(match)

    def updateFinishedMatches(self):
        self.ui.listWidget_2.clear()
        for match in self.category.bracket.finished_matches:
            self.ui.listWidget.addItem(match)
    
    def updateTableSelection(self):
        # Free up previous table
        for table in self.tables:
            if table.runningCategory is not None and table.runningCategory == self.category:
                table.runningCategory = None

        index = self.ui.comboBox.currentIndex()
        self.tables[index].runningCategory = self.category
    

    

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

        # setup the checkable combo box for competitors categories
        self.category_combo_box = CheckableComboBox(parent=self.ui.competitors)  
        self.ui.gridLayout_4.addWidget(self.category_combo_box, 0, 4, 1, 1)

        self.ui.Start.clicked.connect(self.startCategory)
        

        
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


    def startCategory(self):
        categoryIndex = self.ui.categories_2.currentRow()
        competitors =self.competition.getCompetitorsInCategory(self.competition.categories[categoryIndex])
        if len(competitors) > 1 : 
            self.catWindow = CategoryView(self.competition.categories[categoryIndex],self.competition.tables, competitors)
            self.catWindow.show()


    def updateCompetetionUI(self):
        self.ui.ChangeName.setText(self.competition.name)
        self.ui.ChangeDate.setText(self.competition.date)
        self.updateCategoryList()
        self.updateCompetitorList()
        self.updateTableList()
        self.updateCountryList()


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


    def updateCategoryComboBox(self):  
        category_list = self.competition.getCategoryList()
        for category in category_list:
            self.category_combo_box.addItem(category)


    def removeCategory(self):
        index = self.ui.categories_2.currentRow()
        self.ui.categories_2.takeItem(index)
        self.competition.categories.pop(index)
        self.competition.saveCompetition()


    def updateCategoryList(self):
        self.ui.categories_2.clear()
        for category in self.competition.categories:
            self.ui.categories_2.addItem(category.toString())
        self.updateCategoryComboBox()


    def updateCategoryInputs(self):
        index = self.ui.categories_2.currentRow()
        category = self.competition.categories[index]
        self.ui.Age.setText(category.age)
        self.ui.Weight.setText(category.weight)
        self.ui.Hand.setText(category.hand)
        self.ui.Gender.setText(category.gender)


    def addCompetitor(self):
        name = self.ui.Name_2.text()
        categoriesString = self.category_combo_box.chekedItems()
        country = self.ui.country.currentText()
        email = self.ui.email.text()
        competitor = Model.Competitor(len(self.competition.competitors) + 1, name, categoriesString, country, email)
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
        #self.category_combo_box.setText(competitor.category)
        self.ui.country.setCurrentText(competitor.country)
        self.ui.email.setText(competitor.email)


    def updateCompetitorList(self):
        self.ui.competitors_2.clear()
        for competitor in self.competition.competitors:
            self.ui.competitors_2.addItem(competitor.toString())
    

    def addTable(self):
        table = Model.Table(self.ui.Table.text())
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
        self.ui.Table.setText(table.name)

    
    def updateTableList(self):
        self.ui.tables_2.clear()
        for table in self.competition.tables:
            self.ui.tables_2.addItem(table.toString())


    def addCountry(self):
        country = Model.Country(self.ui.countries_name.text())
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
        self.ui.countries_name.setText(country.name)


    def updateCountryList(self):
        self.ui.countriesList.clear()
        counter = 0
        for country in self.competition.countries:
            self.ui.countriesList.addItem(str(counter) + ". " + country.name)
            counter += 1
        self.updateCountryComboBox()
    

    def updateCountryComboBox(self):
        for country in self.competition.countries:
            self.ui.country.addItem(country.name)


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


# new check-able combo box 
class CheckableComboBox(QComboBox): 
  
    # constructor 
    def __init__(self, parent = None): 
        super(CheckableComboBox, self).__init__(parent) 
        self.view().pressed.connect(self.handleItemPressed) 
        self.setModel(QStandardItemModel(self)) 

    count = 0
    # action called when item get checked 
    def do_action(self): 
        pass
  
    # when any item get pressed 
    def handleItemPressed(self, index): 
  
        # getting the item 
        item = self.model().itemFromIndex(index) 
  
        # checking if item is checked 
        if item.checkState() == Qt.CheckState.Checked: 
  
            # making it unchecked 
            item.setCheckState(Qt.CheckState.Unchecked) 
  
        # if not checked 
        else: 
            # making the item checked 
            item.setCheckState(Qt.CheckState.Checked) 
  
            self.count += 1
  
            # call the action 
            self.do_action() 
    
    def chekedItems(self):
        checked_items = []
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        return checked_items