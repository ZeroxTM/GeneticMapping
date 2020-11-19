# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1700, 1075)
        MainWindow.setMinimumSize(QSize(1700, 1000))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"../PycharmProjects/pngegg (49).png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        MainWindow.setIconSize(QSize(20, 20))
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionImport_Map_Data = QAction(MainWindow)
        self.actionImport_Map_Data.setObjectName(u"actionImport_Map_Data")
        icon1 = QIcon()
        icon1.addFile(u"images/importIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport_Map_Data.setIcon(icon1)
        self.actionImport_Existing_Map = QAction(MainWindow)
        self.actionImport_Existing_Map.setObjectName(u"actionImport_Existing_Map")
        self.actionImport_Existing_Map.setIcon(icon1)
        self.actionEdit_Input_Map = QAction(MainWindow)
        self.actionEdit_Input_Map.setObjectName(u"actionEdit_Input_Map")
        icon2 = QIcon()
        icon2.addFile(u"images/editIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit_Input_Map.setIcon(icon2)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon3 = QIcon()
        icon3.addFile(u"images/preferencesIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPreferences.setIcon(icon3)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon4 = QIcon()
        icon4.addFile(u"images/exitIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionCompare_Maps = QAction(MainWindow)
        self.actionCompare_Maps.setObjectName(u"actionCompare_Maps")
        icon5 = QIcon()
        icon5.addFile(u"images/compareIcon2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCompare_Maps.setIcon(icon5)
        font = QFont()
        font.setFamily(u"Georgia")
        self.actionCompare_Maps.setFont(font)
        self.actionCompare_Distances = QAction(MainWindow)
        self.actionCompare_Distances.setObjectName(u"actionCompare_Distances")
        icon6 = QIcon()
        icon6.addFile(u"images/compareIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCompare_Distances.setIcon(icon6)
        self.actionEdit_Genetic_MAp = QAction(MainWindow)
        self.actionEdit_Genetic_MAp.setObjectName(u"actionEdit_Genetic_MAp")
        self.actionEdit_Genetic_MAp.setIcon(icon2)
        self.actionCalculate_Critereon = QAction(MainWindow)
        self.actionCalculate_Critereon.setObjectName(u"actionCalculate_Critereon")
        self.actionTest_Cluster_Linear_Structure = QAction(MainWindow)
        self.actionTest_Cluster_Linear_Structure.setObjectName(u"actionTest_Cluster_Linear_Structure")
        self.actionSubdivide_Cluster_Into = QAction(MainWindow)
        self.actionSubdivide_Cluster_Into.setObjectName(u"actionSubdivide_Cluster_Into")
        self.actionInspect_Parallel_Linkage = QAction(MainWindow)
        self.actionInspect_Parallel_Linkage.setObjectName(u"actionInspect_Parallel_Linkage")
        icon7 = QIcon()
        icon7.addFile(u"images/linkageIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInspect_Parallel_Linkage.setIcon(icon7)
        self.actionExport_Graph = QAction(MainWindow)
        self.actionExport_Graph.setObjectName(u"actionExport_Graph")
        self.actionOpen_Graph_with_Pajek = QAction(MainWindow)
        self.actionOpen_Graph_with_Pajek.setObjectName(u"actionOpen_Graph_with_Pajek")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.myMain = QWidget(MainWindow)
        self.myMain.setObjectName(u"myMain")
        self.myMain.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myMain.sizePolicy().hasHeightForWidth())
        self.myMain.setSizePolicy(sizePolicy)
        self.myMain.setMinimumSize(QSize(1700, 100))
        self.formLayout_2 = QFormLayout(self.myMain)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.browserTab = QTabWidget(self.myMain)
        self.browserTab.setObjectName(u"browserTab")
        sizePolicy.setHeightForWidth(self.browserTab.sizePolicy().hasHeightForWidth())
        self.browserTab.setSizePolicy(sizePolicy)
        self.browserTab.setMinimumSize(QSize(0, 500))
        self.browserTab.setMaximumSize(QSize(16777215, 16777215))
        self.FileBrowserTab = QWidget()
        self.FileBrowserTab.setObjectName(u"FileBrowserTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FileBrowserTab.sizePolicy().hasHeightForWidth())
        self.FileBrowserTab.setSizePolicy(sizePolicy1)
        self.FileBrowserTab.setMinimumSize(QSize(0, 0))
        self.FileBrowserTab.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout_11 = QFormLayout(self.FileBrowserTab)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.widget_2 = QWidget(self.FileBrowserTab)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.formLayout_13 = QFormLayout(self.widget_2)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.browserTreeView = QTreeView(self.widget_2)
        self.browserTreeView.setObjectName(u"browserTreeView")

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.browserTreeView)


        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.widget_2)

        self.browserTab.addTab(self.FileBrowserTab, "")
        self.viewOptionsTab = QWidget()
        self.viewOptionsTab.setObjectName(u"viewOptionsTab")
        self.formLayout_12 = QFormLayout(self.viewOptionsTab)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.pushButton_4 = QPushButton(self.viewOptionsTab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.pushButton_4)

        self.browserTab.addTab(self.viewOptionsTab, "")

        self.horizontalLayout.addWidget(self.browserTab)

        self.line = QFrame(self.myMain)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.mainTabs = QTabWidget(self.myMain)
        self.mainTabs.setObjectName(u"mainTabs")
        sizePolicy1.setHeightForWidth(self.mainTabs.sizePolicy().hasHeightForWidth())
        self.mainTabs.setSizePolicy(sizePolicy1)
        self.mainTabs.setMinimumSize(QSize(0, 500))
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(10)
        self.mainTabs.setFont(font1)
        self.mainTabs.setStyleSheet(u"")
        self.markersTab = QWidget()
        self.markersTab.setObjectName(u"markersTab")
        self.formLayout_4 = QFormLayout(self.markersTab)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.markersTable = QTableWidget(self.markersTab)
        if (self.markersTable.columnCount() < 16):
            self.markersTable.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.markersTable.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        self.markersTable.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        if (self.markersTable.rowCount() < 28):
            self.markersTable.setRowCount(28)
        self.markersTable.setObjectName(u"markersTable")
        sizePolicy1.setHeightForWidth(self.markersTable.sizePolicy().hasHeightForWidth())
        self.markersTable.setSizePolicy(sizePolicy1)
        self.markersTable.setStyleSheet(u"")
        self.markersTable.setFrameShape(QFrame.StyledPanel)
        self.markersTable.setFrameShadow(QFrame.Sunken)
        self.markersTable.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.markersTable.setGridStyle(Qt.SolidLine)
        self.markersTable.setWordWrap(True)
        self.markersTable.setRowCount(28)
        self.markersTable.setColumnCount(16)
        self.markersTable.horizontalHeader().setCascadingSectionResizes(False)
        self.markersTable.horizontalHeader().setMinimumSectionSize(50)
        self.markersTable.horizontalHeader().setDefaultSectionSize(115)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.markersTable)

        self.mainTabs.addTab(self.markersTab, "")
        self.linkagesTab = QWidget()
        self.linkagesTab.setObjectName(u"linkagesTab")
        self.formLayout_5 = QFormLayout(self.linkagesTab)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.linkageTable = QTableWidget(self.linkagesTab)
        if (self.linkageTable.columnCount() < 17):
            self.linkageTable.setColumnCount(17)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(10, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(11, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(12, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(13, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(14, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(15, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.linkageTable.setHorizontalHeaderItem(16, __qtablewidgetitem32)
        if (self.linkageTable.rowCount() < 20):
            self.linkageTable.setRowCount(20)
        self.linkageTable.setObjectName(u"linkageTable")
        self.linkageTable.setFrameShape(QFrame.StyledPanel)
        self.linkageTable.setRowCount(20)
        self.linkageTable.horizontalHeader().setCascadingSectionResizes(False)
        self.linkageTable.horizontalHeader().setDefaultSectionSize(125)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.linkageTable)

        self.mainTabs.addTab(self.linkagesTab, "")
        self.networkTab = QWidget()
        self.networkTab.setObjectName(u"networkTab")
        self.formLayout_6 = QFormLayout(self.networkTab)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_2 = QLabel(self.networkTab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.mainTabs.addTab(self.networkTab, "")
        self.genotypingTab = QWidget()
        self.genotypingTab.setObjectName(u"genotypingTab")
        self.formLayout_7 = QFormLayout(self.genotypingTab)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.pushButton = QPushButton(self.genotypingTab)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.pushButton)

        self.mainTabs.addTab(self.genotypingTab, "")
        self.geneticMapTab = QWidget()
        self.geneticMapTab.setObjectName(u"geneticMapTab")
        self.formLayout_8 = QFormLayout(self.geneticMapTab)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.pushButton_2 = QPushButton(self.geneticMapTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.pushButton_2)

        self.mainTabs.addTab(self.geneticMapTab, "")
        self.comparisionTab = QWidget()
        self.comparisionTab.setObjectName(u"comparisionTab")
        self.formLayout_9 = QFormLayout(self.comparisionTab)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.pushButton_3 = QPushButton(self.comparisionTab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.pushButton_3)

        self.mainTabs.addTab(self.comparisionTab, "")

        self.horizontalLayout.addWidget(self.mainTabs)

        self.line_2 = QFrame(self.myMain)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.statisticsTab = QTabWidget(self.myMain)
        self.statisticsTab.setObjectName(u"statisticsTab")
        sizePolicy.setHeightForWidth(self.statisticsTab.sizePolicy().hasHeightForWidth())
        self.statisticsTab.setSizePolicy(sizePolicy)
        self.statisticsTab.setMinimumSize(QSize(350, 0))
        self.statisticsTab.setMaximumSize(QSize(350, 16777215))
        self.statisticsTab.setStyleSheet(u"background-color: rgb(224, 224, 224);")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        sizePolicy1.setHeightForWidth(self.tab_7.sizePolicy().hasHeightForWidth())
        self.tab_7.setSizePolicy(sizePolicy1)
        self.tab_7.setMinimumSize(QSize(0, 0))
        self.tab_7.setMaximumSize(QSize(16777215, 922))
        self.formLayout_10 = QFormLayout(self.tab_7)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(50)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.groupBox = QGroupBox(self.tab_7)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(300, 200))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.groupBox.setFont(font3)
        self.groupBox.setFlat(True)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 5, -1)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setFamily(u"Georgia")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.gridLayout)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(-1, 0, 5, -1)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_9, 3, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_10, 4, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font3)
        self.groupBox_3.setFlat(True)
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(15)
        self.gridLayout_4.setContentsMargins(-1, -1, 5, 1)
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_23, 2, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setCheckable(False)

        self.gridLayout_4.addWidget(self.checkBox_2, 3, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_15.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox_3)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_16.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_14.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_14, 0, 1, 1, 1)


        self.formLayout_3.setLayout(0, QFormLayout.SpanningRole, self.gridLayout_4)


        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.formLayout_10.setLayout(0, QFormLayout.SpanningRole, self.gridLayout_5)

        self.statisticsTab.addTab(self.tab_7, "")

        self.horizontalLayout.addWidget(self.statisticsTab)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.importStatus = QLabel(self.myMain)
        self.importStatus.setObjectName(u"importStatus")
        sizePolicy.setHeightForWidth(self.importStatus.sizePolicy().hasHeightForWidth())
        self.importStatus.setSizePolicy(sizePolicy)
        self.importStatus.setMinimumSize(QSize(50, 30))
        self.importStatus.setMaximumSize(QSize(200, 30))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setBold(True)
        font5.setWeight(75)
        self.importStatus.setFont(font5)
        self.importStatus.setLayoutDirection(Qt.LeftToRight)
        self.importStatus.setFrameShape(QFrame.NoFrame)
        self.importStatus.setFrameShadow(QFrame.Plain)
        self.importStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.importStatus.setWordWrap(False)

        self.gridLayout_6.addWidget(self.importStatus, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout)

        MainWindow.setCentralWidget(self.myMain)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1700, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuMap_Testing = QMenu(self.menubar)
        self.menuMap_Testing.setObjectName(u"menuMap_Testing")
        self.menuNetwok_Of_Linkages = QMenu(self.menubar)
        self.menuNetwok_Of_Linkages.setObjectName(u"menuNetwok_Of_Linkages")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMap_Testing.menuAction())
        self.menubar.addAction(self.menuNetwok_Of_Linkages.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport_Map_Data)
        self.menuFile.addAction(self.actionImport_Existing_Map)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEdit_Input_Map)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionQuit)
        self.menuMap_Testing.addAction(self.actionCompare_Maps)
        self.menuMap_Testing.addAction(self.actionCompare_Distances)
        self.menuMap_Testing.addSeparator()
        self.menuMap_Testing.addAction(self.actionEdit_Genetic_MAp)
        self.menuMap_Testing.addAction(self.actionCalculate_Critereon)
        self.menuMap_Testing.addSeparator()
        self.menuMap_Testing.addAction(self.actionTest_Cluster_Linear_Structure)
        self.menuMap_Testing.addAction(self.actionSubdivide_Cluster_Into)
        self.menuNetwok_Of_Linkages.addAction(self.actionInspect_Parallel_Linkage)
        self.menuNetwok_Of_Linkages.addAction(self.actionExport_Graph)
        self.menuNetwok_Of_Linkages.addAction(self.actionOpen_Graph_with_Pajek)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.browserTab.setCurrentIndex(0)
        self.mainTabs.setCurrentIndex(0)
        self.statisticsTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Genetic Mapping", None))
        self.actionImport_Map_Data.setText(QCoreApplication.translate("MainWindow", u"Import Map Data", None))
        self.actionImport_Existing_Map.setText(QCoreApplication.translate("MainWindow", u"Import Existing Map", None))
        self.actionEdit_Input_Map.setText(QCoreApplication.translate("MainWindow", u"Edit Input Map", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCompare_Maps.setText(QCoreApplication.translate("MainWindow", u"Compare Maps", None))
        self.actionCompare_Distances.setText(QCoreApplication.translate("MainWindow", u"Compare Distances", None))
        self.actionEdit_Genetic_MAp.setText(QCoreApplication.translate("MainWindow", u"Edit Genetic MAp", None))
        self.actionCalculate_Critereon.setText(QCoreApplication.translate("MainWindow", u"Calculate Critereon", None))
        self.actionTest_Cluster_Linear_Structure.setText(QCoreApplication.translate("MainWindow", u"Test Cluster Linear Structure", None))
        self.actionSubdivide_Cluster_Into.setText(QCoreApplication.translate("MainWindow", u"Subdivide Cluster Into Linear Topology Parts", None))
        self.actionInspect_Parallel_Linkage.setText(QCoreApplication.translate("MainWindow", u"Inspect Parallel Linkage", None))
        self.actionExport_Graph.setText(QCoreApplication.translate("MainWindow", u"Export Graph", None))
        self.actionOpen_Graph_with_Pajek.setText(QCoreApplication.translate("MainWindow", u"Open Graph with Pajek", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.browserTab.setTabText(self.browserTab.indexOf(self.FileBrowserTab), QCoreApplication.translate("MainWindow", u"File Directory", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.browserTab.setTabText(self.browserTab.indexOf(self.viewOptionsTab), QCoreApplication.translate("MainWindow", u"View Options", None))
        ___qtablewidgetitem = self.markersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Marker ID", None));
        ___qtablewidgetitem1 = self.markersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.markersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Allele", None));
        ___qtablewidgetitem3 = self.markersTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"n0", None));
        ___qtablewidgetitem4 = self.markersTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"n1", None));
        ___qtablewidgetitem5 = self.markersTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"nMissing", None));
        ___qtablewidgetitem6 = self.markersTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"p0", None));
        ___qtablewidgetitem7 = self.markersTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"p1", None));
        ___qtablewidgetitem8 = self.markersTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"pMissing", None));
        ___qtablewidgetitem9 = self.markersTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Segregation", None));
        ___qtablewidgetitem10 = self.markersTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Twins", None));
        ___qtablewidgetitem11 = self.markersTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"LG ID", None));
        ___qtablewidgetitem12 = self.markersTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"LG", None));
        ___qtablewidgetitem13 = self.markersTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Topology Index", None));
        ___qtablewidgetitem14 = self.markersTable.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Skeleton Index", None));
        ___qtablewidgetitem15 = self.markersTable.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Genetic Coordinates", None));
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.markersTab), QCoreApplication.translate("MainWindow", u"Markers", None))
        ___qtablewidgetitem16 = self.linkageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Linkage ID", None));
        ___qtablewidgetitem17 = self.linkageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Marker 1 ID", None));
        ___qtablewidgetitem18 = self.linkageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Marker 2 ID", None));
        ___qtablewidgetitem19 = self.linkageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Marker 1 Name", None));
        ___qtablewidgetitem20 = self.linkageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Marker 2 Name", None));
        ___qtablewidgetitem21 = self.linkageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"n00,n01,n10,n11", None));
        ___qtablewidgetitem22 = self.linkageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Recombination Rate", None));
        ___qtablewidgetitem23 = self.linkageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Haldane Distance", None));
        ___qtablewidgetitem24 = self.linkageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Kossambi Distance", None));
        ___qtablewidgetitem25 = self.linkageTable.horizontalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Observed Distance", None));
        ___qtablewidgetitem26 = self.linkageTable.horizontalHeaderItem(10)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Distance On Map", None));
        ___qtablewidgetitem27 = self.linkageTable.horizontalHeaderItem(11)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"p Value", None));
        ___qtablewidgetitem28 = self.linkageTable.horizontalHeaderItem(12)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"p Min", None));
        ___qtablewidgetitem29 = self.linkageTable.horizontalHeaderItem(13)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"p Max", None));
        ___qtablewidgetitem30 = self.linkageTable.horizontalHeaderItem(14)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Min Haldane Distance", None));
        ___qtablewidgetitem31 = self.linkageTable.horizontalHeaderItem(15)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Max Haldane Distance", None));
        ___qtablewidgetitem32 = self.linkageTable.horizontalHeaderItem(16)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Connection Index", None));
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.linkagesTab), QCoreApplication.translate("MainWindow", u"Linkages", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Network Structure Quick Preview", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.networkTab), QCoreApplication.translate("MainWindow", u"Network Structure", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.genotypingTab), QCoreApplication.translate("MainWindow", u"Graphical Genotyping ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.geneticMapTab), QCoreApplication.translate("MainWindow", u"Genetic Map", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.comparisionTab), QCoreApplication.translate("MainWindow", u"Map Comparision ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Genotypes count[0,1,-1]:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number of Markers:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number of Linkage Groups:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Recombination Frequency:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Allele Frequency:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Marker Statistics", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Genotype:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Skeleton Index:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Marker ID:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Genotype Cords:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Linkage Group", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total number of markers:", None))
        self.checkBox_2.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Linkage Group ID:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Skeleton Marker:", None))
        self.statisticsTab.setTabText(self.statisticsTab.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.importStatus.setText(QCoreApplication.translate("MainWindow", u"No Data has been imported yet", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMap_Testing.setTitle(QCoreApplication.translate("MainWindow", u"Map Testing", None))
        self.menuNetwok_Of_Linkages.setTitle(QCoreApplication.translate("MainWindow", u"Netwok Of Linkages", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.text_box.setPlainText('test')  # here we are addressing widget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())