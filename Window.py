# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 868)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.CreateNewCompetetion = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateNewCompetetion.sizePolicy().hasHeightForWidth())
        self.CreateNewCompetetion.setSizePolicy(sizePolicy)
        self.CreateNewCompetetion.setObjectName("CreateNewCompetetion")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CreateNewCompetetion)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CompetetionName = QtWidgets.QLineEdit(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompetetionName.sizePolicy().hasHeightForWidth())
        self.CompetetionName.setSizePolicy(sizePolicy)
        self.CompetetionName.setObjectName("CompetetionName")
        self.gridLayout_2.addWidget(self.CompetetionName, 1, 4, 1, 1)
        self.Create = QtWidgets.QPushButton(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Create.sizePolicy().hasHeightForWidth())
        self.Create.setSizePolicy(sizePolicy)
        self.Create.setObjectName("Create")
        self.gridLayout_2.addWidget(self.Create, 8, 4, 1, 1)
        self.LoadCompetetion = QtWidgets.QPushButton(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadCompetetion.sizePolicy().hasHeightForWidth())
        self.LoadCompetetion.setSizePolicy(sizePolicy)
        self.LoadCompetetion.setObjectName("LoadCompetetion")
        self.gridLayout_2.addWidget(self.LoadCompetetion, 11, 4, 1, 1)
        self.Name = QtWidgets.QLabel(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setObjectName("Name")
        self.gridLayout_2.addWidget(self.Name, 1, 0, 1, 1)
        self.CompetitionDate = QtWidgets.QLineEdit(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompetitionDate.sizePolicy().hasHeightForWidth())
        self.CompetitionDate.setSizePolicy(sizePolicy)
        self.CompetitionDate.setObjectName("CompetitionDate")
        self.gridLayout_2.addWidget(self.CompetitionDate, 7, 4, 1, 1)
        self.Date = QtWidgets.QLabel(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Date.sizePolicy().hasHeightForWidth())
        self.Date.setSizePolicy(sizePolicy)
        self.Date.setObjectName("Date")
        self.gridLayout_2.addWidget(self.Date, 7, 0, 1, 1)
        self.createCompetetion = QtWidgets.QLabel(parent=self.CreateNewCompetetion)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createCompetetion.sizePolicy().hasHeightForWidth())
        self.createCompetetion.setSizePolicy(sizePolicy)
        self.createCompetetion.setObjectName("createCompetetion")
        self.gridLayout_2.addWidget(self.createCompetetion, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.CreateNewCompetetion, 3, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.competition = QtWidgets.QWidget()
        self.competition.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.competition.sizePolicy().hasHeightForWidth())
        self.competition.setSizePolicy(sizePolicy)
        self.competition.setMinimumSize(QtCore.QSize(797, 0))
        self.competition.setObjectName("competition")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.competition)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ChangeName = QtWidgets.QLineEdit(parent=self.competition)
        self.ChangeName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangeName.sizePolicy().hasHeightForWidth())
        self.ChangeName.setSizePolicy(sizePolicy)
        self.ChangeName.setText("")
        self.ChangeName.setObjectName("ChangeName")
        self.gridLayout_3.addWidget(self.ChangeName, 0, 1, 1, 1)
        self.saveCompetetion = QtWidgets.QPushButton(parent=self.competition)
        self.saveCompetetion.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveCompetetion.sizePolicy().hasHeightForWidth())
        self.saveCompetetion.setSizePolicy(sizePolicy)
        self.saveCompetetion.setMouseTracking(True)
        self.saveCompetetion.setAcceptDrops(True)
        self.saveCompetetion.setCheckable(False)
        self.saveCompetetion.setAutoDefault(False)
        self.saveCompetetion.setObjectName("saveCompetetion")
        self.gridLayout_3.addWidget(self.saveCompetetion, 2, 1, 1, 1)
        self.Name_7 = QtWidgets.QLabel(parent=self.competition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name_7.sizePolicy().hasHeightForWidth())
        self.Name_7.setSizePolicy(sizePolicy)
        self.Name_7.setObjectName("Name_7")
        self.gridLayout_3.addWidget(self.Name_7, 0, 0, 1, 1)
        self.Date_7 = QtWidgets.QLabel(parent=self.competition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Date_7.sizePolicy().hasHeightForWidth())
        self.Date_7.setSizePolicy(sizePolicy)
        self.Date_7.setObjectName("Date_7")
        self.gridLayout_3.addWidget(self.Date_7, 1, 0, 1, 1)
        self.ChangeDate = QtWidgets.QLineEdit(parent=self.competition)
        self.ChangeDate.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangeDate.sizePolicy().hasHeightForWidth())
        self.ChangeDate.setSizePolicy(sizePolicy)
        self.ChangeDate.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.ChangeDate.setAccessibleDescription("")
        self.ChangeDate.setAutoFillBackground(False)
        self.ChangeDate.setObjectName("ChangeDate")
        self.gridLayout_3.addWidget(self.ChangeDate, 1, 1, 1, 1)
        self.Name_7.raise_()
        self.Date_7.raise_()
        self.ChangeDate.raise_()
        self.saveCompetetion.raise_()
        self.ChangeName.raise_()
        self.tabWidget.addTab(self.competition, "")
        self.categories = QtWidgets.QWidget()
        self.categories.setObjectName("categories")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.categories)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Remove_2 = QtWidgets.QPushButton(parent=self.categories)
        self.Remove_2.setObjectName("Remove_2")
        self.gridLayout_5.addWidget(self.Remove_2, 1, 8, 1, 1)
        self.Date_5 = QtWidgets.QLabel(parent=self.categories)
        self.Date_5.setObjectName("Date_5")
        self.gridLayout_5.addWidget(self.Date_5, 0, 4, 1, 1)
        self.UpdateCategory = QtWidgets.QPushButton(parent=self.categories)
        self.UpdateCategory.setObjectName("UpdateCategory")
        self.gridLayout_5.addWidget(self.UpdateCategory, 0, 8, 1, 1)
        self.Name_9 = QtWidgets.QLabel(parent=self.categories)
        self.Name_9.setObjectName("Name_9")
        self.gridLayout_5.addWidget(self.Name_9, 0, 0, 1, 1)
        self.Age = QtWidgets.QLineEdit(parent=self.categories)
        self.Age.setObjectName("Age")
        self.gridLayout_5.addWidget(self.Age, 0, 1, 1, 1)
        self.Name_5 = QtWidgets.QLabel(parent=self.categories)
        self.Name_5.setObjectName("Name_5")
        self.gridLayout_5.addWidget(self.Name_5, 0, 2, 1, 1)
        self.Weight = QtWidgets.QLineEdit(parent=self.categories)
        self.Weight.setObjectName("Weight")
        self.gridLayout_5.addWidget(self.Weight, 0, 3, 1, 1)
        self.Hand = QtWidgets.QLineEdit(parent=self.categories)
        self.Hand.setObjectName("Hand")
        self.gridLayout_5.addWidget(self.Hand, 0, 5, 1, 1)
        self.Date_6 = QtWidgets.QLabel(parent=self.categories)
        self.Date_6.setObjectName("Date_6")
        self.gridLayout_5.addWidget(self.Date_6, 0, 6, 1, 1)
        self.Gender = QtWidgets.QLineEdit(parent=self.categories)
        self.Gender.setObjectName("Gender")
        self.gridLayout_5.addWidget(self.Gender, 0, 7, 1, 1)
        self.categories_2 = QtWidgets.QListWidget(parent=self.categories)
        self.categories_2.setObjectName("categories_2")
        self.gridLayout_5.addWidget(self.categories_2, 2, 0, 1, 9)
        self.tabWidget.addTab(self.categories, "")
        self.competitors = QtWidgets.QWidget()
        self.competitors.setObjectName("competitors")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.competitors)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Name_11 = QtWidgets.QLabel(parent=self.competitors)
        self.Name_11.setObjectName("Name_11")
        self.gridLayout_4.addWidget(self.Name_11, 0, 0, 1, 1)
        self.Name_2 = QtWidgets.QLineEdit(parent=self.competitors)
        self.Name_2.setObjectName("Name_2")
        self.gridLayout_4.addWidget(self.Name_2, 0, 1, 1, 1)
        self.Name_13 = QtWidgets.QLabel(parent=self.competitors)
        self.Name_13.setObjectName("Name_13")
        self.gridLayout_4.addWidget(self.Name_13, 0, 2, 1, 1)
        self.Categories = QtWidgets.QLineEdit(parent=self.competitors)
        self.Categories.setObjectName("Categories")
        self.gridLayout_4.addWidget(self.Categories, 0, 3, 1, 1)
        self.Update = QtWidgets.QPushButton(parent=self.competitors)
        self.Update.setObjectName("Update")
        self.gridLayout_4.addWidget(self.Update, 0, 4, 1, 1)
        self.Name_12 = QtWidgets.QLabel(parent=self.competitors)
        self.Name_12.setObjectName("Name_12")
        self.gridLayout_4.addWidget(self.Name_12, 1, 0, 1, 1)
        self.Country = QtWidgets.QLineEdit(parent=self.competitors)
        self.Country.setObjectName("Country")
        self.gridLayout_4.addWidget(self.Country, 1, 1, 1, 1)
        self.Name_14 = QtWidgets.QLabel(parent=self.competitors)
        self.Name_14.setObjectName("Name_14")
        self.gridLayout_4.addWidget(self.Name_14, 1, 2, 1, 1)
        self.email = QtWidgets.QLineEdit(parent=self.competitors)
        self.email.setObjectName("email")
        self.gridLayout_4.addWidget(self.email, 1, 3, 1, 1)
        self.Remove = QtWidgets.QPushButton(parent=self.competitors)
        self.Remove.setObjectName("Remove")
        self.gridLayout_4.addWidget(self.Remove, 1, 4, 1, 1)
        self.competitors_2 = QtWidgets.QListWidget(parent=self.competitors)
        self.competitors_2.setObjectName("competitors_2")
        self.gridLayout_4.addWidget(self.competitors_2, 2, 0, 1, 5)
        self.tabWidget.addTab(self.competitors, "")
        self.tables = QtWidgets.QWidget()
        self.tables.setObjectName("tables")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tables)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Name_10 = QtWidgets.QLabel(parent=self.tables)
        self.Name_10.setObjectName("Name_10")
        self.gridLayout_6.addWidget(self.Name_10, 0, 0, 1, 1)
        self.Table = QtWidgets.QLineEdit(parent=self.tables)
        self.Table.setObjectName("Table")
        self.gridLayout_6.addWidget(self.Table, 0, 1, 1, 1)
        self.UpdateTable = QtWidgets.QPushButton(parent=self.tables)
        self.UpdateTable.setObjectName("UpdateTable")
        self.gridLayout_6.addWidget(self.UpdateTable, 0, 2, 1, 1)
        self.countries_name = QtWidgets.QLineEdit(parent=self.tables)
        self.countries_name.setObjectName("countries_name")
        self.gridLayout_6.addWidget(self.countries_name, 0, 3, 1, 1)
        self.UpdateCountry = QtWidgets.QPushButton(parent=self.tables)
        self.UpdateCountry.setObjectName("UpdateCountry")
        self.gridLayout_6.addWidget(self.UpdateCountry, 0, 4, 1, 1)
        self.Name_15 = QtWidgets.QLabel(parent=self.tables)
        self.Name_15.setObjectName("Name_15")
        self.gridLayout_6.addWidget(self.Name_15, 1, 1, 1, 1)
        self.Remove_3 = QtWidgets.QPushButton(parent=self.tables)
        self.Remove_3.setObjectName("Remove_3")
        self.gridLayout_6.addWidget(self.Remove_3, 1, 2, 1, 1)
        self.Name_16 = QtWidgets.QLabel(parent=self.tables)
        self.Name_16.setObjectName("Name_16")
        self.gridLayout_6.addWidget(self.Name_16, 1, 3, 1, 1)
        self.Remove_4 = QtWidgets.QPushButton(parent=self.tables)
        self.Remove_4.setObjectName("Remove_4")
        self.gridLayout_6.addWidget(self.Remove_4, 1, 4, 1, 1)
        self.tables_2 = QtWidgets.QListWidget(parent=self.tables)
        self.tables_2.setObjectName("tables_2")
        self.gridLayout_6.addWidget(self.tables_2, 2, 0, 1, 2)
        self.countriesList = QtWidgets.QListWidget(parent=self.tables)
        self.countriesList.setObjectName("countriesList")
        self.gridLayout_6.addWidget(self.countriesList, 2, 3, 1, 1)
        self.tabWidget.addTab(self.tables, "")
        self.results = QtWidgets.QWidget()
        self.results.setObjectName("results")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.results)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.results_2 = QtWidgets.QListView(parent=self.results)
        self.results_2.setObjectName("results_2")
        self.gridLayout_7.addWidget(self.results_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.results, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 3, 1)
        self.CreateNewCompetetion.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Competetion = QtGui.QAction(parent=MainWindow)
        self.actionNew_Competetion.setObjectName("actionNew_Competetion")
        self.actionLoad_Competetion = QtGui.QAction(parent=MainWindow)
        self.actionLoad_Competetion.setObjectName("actionLoad_Competetion")
        self.menuFile.addAction(self.actionNew_Competetion)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Competetion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Create.setText(_translate("MainWindow", "Create"))
        self.LoadCompetetion.setText(_translate("MainWindow", "Load Competition from file"))
        self.Name.setText(_translate("MainWindow", "Name:"))
        self.Date.setText(_translate("MainWindow", "Date:"))
        self.createCompetetion.setText(_translate("MainWindow", "Create new competetion"))
        self.saveCompetetion.setText(_translate("MainWindow", "save"))
        self.Name_7.setText(_translate("MainWindow", "Name:"))
        self.Date_7.setText(_translate("MainWindow", "Date:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.competition), _translate("MainWindow", "competition"))
        self.Remove_2.setText(_translate("MainWindow", "Remove"))
        self.Date_5.setText(_translate("MainWindow", "Hand:"))
        self.UpdateCategory.setText(_translate("MainWindow", "Update"))
        self.Name_9.setText(_translate("MainWindow", "Age:"))
        self.Name_5.setText(_translate("MainWindow", "Weight:"))
        self.Date_6.setText(_translate("MainWindow", "Gender:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.categories), _translate("MainWindow", "categories"))
        self.Name_11.setText(_translate("MainWindow", "Name:"))
        self.Name_13.setText(_translate("MainWindow", "Categories:"))
        self.Update.setText(_translate("MainWindow", "Update"))
        self.Name_12.setText(_translate("MainWindow", "Country:"))
        self.Name_14.setText(_translate("MainWindow", "Email:"))
        self.Remove.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.competitors), _translate("MainWindow", "competitors"))
        self.Name_10.setText(_translate("MainWindow", "Name:"))
        self.UpdateTable.setText(_translate("MainWindow", "Update"))
        self.UpdateCountry.setText(_translate("MainWindow", "Update"))
        self.Name_15.setText(_translate("MainWindow", "Tables"))
        self.Remove_3.setText(_translate("MainWindow", "Remove"))
        self.Name_16.setText(_translate("MainWindow", "Countries"))
        self.Remove_4.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), _translate("MainWindow", "tables/countries"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results), _translate("MainWindow", "results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_Competetion.setText(_translate("MainWindow", "New Competetion"))
        self.actionLoad_Competetion.setText(_translate("MainWindow", "Load Competetion"))
