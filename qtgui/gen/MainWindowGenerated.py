# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cooki\OneDrive\Documents\workspace_home\projects\pyramidbar\qtgui\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalFrame_2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_all = QtWidgets.QPushButton(self.verticalFrame_2)
        self.pushButton_all.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_all.sizePolicy().hasHeightForWidth())
        self.pushButton_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_all.setFont(font)
        self.pushButton_all.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_all.setObjectName("pushButton_all")
        self.verticalLayout_2.addWidget(self.pushButton_all)
        self.pushButton_rum = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rum.sizePolicy().hasHeightForWidth())
        self.pushButton_rum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rum.setFont(font)
        self.pushButton_rum.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_rum.setObjectName("pushButton_rum")
        self.verticalLayout_2.addWidget(self.pushButton_rum)
        self.pushButton_whiskey = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_whiskey.sizePolicy().hasHeightForWidth())
        self.pushButton_whiskey.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_whiskey.setFont(font)
        self.pushButton_whiskey.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_whiskey.setObjectName("pushButton_whiskey")
        self.verticalLayout_2.addWidget(self.pushButton_whiskey)
        self.pushButton_vodka = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_vodka.sizePolicy().hasHeightForWidth())
        self.pushButton_vodka.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_vodka.setFont(font)
        self.pushButton_vodka.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_vodka.setObjectName("pushButton_vodka")
        self.verticalLayout_2.addWidget(self.pushButton_vodka)
        self.pushButton_gin = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gin.sizePolicy().hasHeightForWidth())
        self.pushButton_gin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gin.setFont(font)
        self.pushButton_gin.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_gin.setObjectName("pushButton_gin")
        self.verticalLayout_2.addWidget(self.pushButton_gin)
        self.pushButton_amaretto = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_amaretto.sizePolicy().hasHeightForWidth())
        self.pushButton_amaretto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_amaretto.setFont(font)
        self.pushButton_amaretto.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_amaretto.setObjectName("pushButton_amaretto")
        self.verticalLayout_2.addWidget(self.pushButton_amaretto)
        self.pushButton_cocktails = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cocktails.sizePolicy().hasHeightForWidth())
        self.pushButton_cocktails.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cocktails.setFont(font)
        self.pushButton_cocktails.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_cocktails.setObjectName("pushButton_cocktails")
        self.verticalLayout_2.addWidget(self.pushButton_cocktails)
        self.pushButton_beer = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_beer.sizePolicy().hasHeightForWidth())
        self.pushButton_beer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_beer.setFont(font)
        self.pushButton_beer.setStyleSheet("QPushButton{background-color: rgb(220,179,179)}")
        self.pushButton_beer.setObjectName("pushButton_beer")
        self.verticalLayout_2.addWidget(self.pushButton_beer)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.tableWidget_menu = QtWidgets.QTableWidget(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_menu.sizePolicy().hasHeightForWidth())
        self.tableWidget_menu.setSizePolicy(sizePolicy)
        self.tableWidget_menu.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_menu.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_menu.setFont(font)
        self.tableWidget_menu.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_menu.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_menu.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_menu.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_menu.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_menu.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_menu.setRowCount(0)
        self.tableWidget_menu.setColumnCount(2)
        self.tableWidget_menu.setObjectName("tableWidget_menu")
        self.tableWidget_menu.horizontalHeader().setVisible(False)
        self.tableWidget_menu.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_menu.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_menu.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_menu)
        self.horizontalLayout_3.addWidget(self.verticalFrame_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.tableWidget_till = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_till.sizePolicy().hasHeightForWidth())
        self.tableWidget_till.setSizePolicy(sizePolicy)
        self.tableWidget_till.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget_till.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_till.setFont(font)
        self.tableWidget_till.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_till.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_till.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_till.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_till.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_till.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_till.setRowCount(0)
        self.tableWidget_till.setColumnCount(2)
        self.tableWidget_till.setObjectName("tableWidget_till")
        self.tableWidget_till.horizontalHeader().setVisible(False)
        self.tableWidget_till.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_till.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_till.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tableWidget_till)
        spacerItem = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_total_value = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_value.setFont(font)
        self.label_total_value.setObjectName("label_total_value")
        self.horizontalLayout_5.addWidget(self.label_total_value)
        self.verticalLayout_4.addWidget(self.horizontalFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_4.addWidget(self.pushButton_clear)
        self.pushButton_remove_item = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove_item.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_remove_item.setFont(font)
        self.pushButton_remove_item.setObjectName("pushButton_remove_item")
        self.verticalLayout_4.addWidget(self.pushButton_remove_item)
        self.pushButton_manual_item = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manual_item.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_manual_item.setFont(font)
        self.pushButton_manual_item.setObjectName("pushButton_manual_item")
        self.verticalLayout_4.addWidget(self.pushButton_manual_item)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tableWidget_tabs = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_tabs.sizePolicy().hasHeightForWidth())
        self.tableWidget_tabs.setSizePolicy(sizePolicy)
        self.tableWidget_tabs.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget_tabs.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_tabs.setFont(font)
        self.tableWidget_tabs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_tabs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_tabs.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_tabs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_tabs.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_tabs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_tabs.setRowCount(0)
        self.tableWidget_tabs.setColumnCount(2)
        self.tableWidget_tabs.setObjectName("tableWidget_tabs")
        self.tableWidget_tabs.horizontalHeader().setVisible(False)
        self.tableWidget_tabs.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_tabs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tabs.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget_tabs)
        self.pushButton_charge = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_charge.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_charge.setFont(font)
        self.pushButton_charge.setStyleSheet("QPushButton{background-color: rgb(171,255,122)}")
        self.pushButton_charge.setObjectName("pushButton_charge")
        self.verticalLayout_3.addWidget(self.pushButton_charge)
        self.pushButton_top_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_top_up.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_top_up.setFont(font)
        self.pushButton_top_up.setStyleSheet("")
        self.pushButton_top_up.setObjectName("pushButton_top_up")
        self.verticalLayout_3.addWidget(self.pushButton_top_up)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.textEdit_history = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_history.setMinimumSize(QtCore.QSize(210, 0))
        self.textEdit_history.setMaximumSize(QtCore.QSize(16777215, 7777777))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_history.setFont(font)
        self.textEdit_history.setReadOnly(True)
        self.textEdit_history.setObjectName("textEdit_history")
        self.verticalLayout_5.addWidget(self.textEdit_history)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1063, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuDeveloper = QtWidgets.QMenu(self.menuBar)
        self.menuDeveloper.setObjectName("menuDeveloper")
        self.menuLog_Level = QtWidgets.QMenu(self.menuDeveloper)
        self.menuLog_Level.setObjectName("menuLog_Level")
        self.menuTabs = QtWidgets.QMenu(self.menuBar)
        self.menuTabs.setObjectName("menuTabs")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDISABLE = QtWidgets.QAction(MainWindow)
        self.actionDISABLE.setCheckable(True)
        self.actionDISABLE.setObjectName("actionDISABLE")
        self.actionWARNING = QtWidgets.QAction(MainWindow)
        self.actionWARNING.setCheckable(True)
        self.actionWARNING.setObjectName("actionWARNING")
        self.actionINFO = QtWidgets.QAction(MainWindow)
        self.actionINFO.setCheckable(True)
        self.actionINFO.setObjectName("actionINFO")
        self.actionDEBUG = QtWidgets.QAction(MainWindow)
        self.actionDEBUG.setCheckable(True)
        self.actionDEBUG.setObjectName("actionDEBUG")
        self.actionVERBOSE = QtWidgets.QAction(MainWindow)
        self.actionVERBOSE.setCheckable(True)
        self.actionVERBOSE.setObjectName("actionVERBOSE")
        self.actionToggle_developer_log = QtWidgets.QAction(MainWindow)
        self.actionToggle_developer_log.setCheckable(True)
        self.actionToggle_developer_log.setObjectName("actionToggle_developer_log")
        self.actionReset_all_tabs = QtWidgets.QAction(MainWindow)
        self.actionReset_all_tabs.setObjectName("actionReset_all_tabs")
        self.actionAdd_patron = QtWidgets.QAction(MainWindow)
        self.actionAdd_patron.setObjectName("actionAdd_patron")
        self.actionRemove_patron = QtWidgets.QAction(MainWindow)
        self.actionRemove_patron.setObjectName("actionRemove_patron")
        self.action_update_tabs_from_file = QtWidgets.QAction(MainWindow)
        self.action_update_tabs_from_file.setObjectName("action_update_tabs_from_file")
        self.action_manually_set_tab = QtWidgets.QAction(MainWindow)
        self.action_manually_set_tab.setObjectName("action_manually_set_tab")
        self.menuLog_Level.addAction(self.actionDISABLE)
        self.menuLog_Level.addAction(self.actionWARNING)
        self.menuLog_Level.addAction(self.actionINFO)
        self.menuLog_Level.addAction(self.actionDEBUG)
        self.menuLog_Level.addAction(self.actionVERBOSE)
        self.menuDeveloper.addAction(self.menuLog_Level.menuAction())
        self.menuDeveloper.addAction(self.actionToggle_developer_log)
        self.menuDeveloper.addAction(self.action_update_tabs_from_file)
        self.menuTabs.addAction(self.actionAdd_patron)
        self.menuTabs.addAction(self.actionRemove_patron)
        self.menuTabs.addAction(self.action_manually_set_tab)
        self.menuBar.addAction(self.menuDeveloper.menuAction())
        self.menuBar.addAction(self.menuTabs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyramidbar"))
        self.pushButton_all.setText(_translate("MainWindow", "All"))
        self.pushButton_rum.setText(_translate("MainWindow", "Rum"))
        self.pushButton_whiskey.setText(_translate("MainWindow", "Whiskey"))
        self.pushButton_vodka.setText(_translate("MainWindow", "Vodka"))
        self.pushButton_gin.setText(_translate("MainWindow", "Gin"))
        self.pushButton_amaretto.setText(_translate("MainWindow", "Amaretto"))
        self.pushButton_cocktails.setText(_translate("MainWindow", "Cocktails"))
        self.pushButton_beer.setText(_translate("MainWindow", "Beer"))
        self.label_2.setText(_translate("MainWindow", "Till"))
        self.label_3.setText(_translate("MainWindow", "Total "))
        self.label_total_value.setText(_translate("MainWindow", "0.00"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_remove_item.setText(_translate("MainWindow", "Remove Item"))
        self.pushButton_manual_item.setText(_translate("MainWindow", "Manual Item"))
        self.label.setText(_translate("MainWindow", "Tabs"))
        self.pushButton_charge.setText(_translate("MainWindow", "Charge"))
        self.pushButton_top_up.setText(_translate("MainWindow", "Top-up"))
        self.label_4.setText(_translate("MainWindow", "History"))
        self.menuDeveloper.setTitle(_translate("MainWindow", "Developer"))
        self.menuLog_Level.setTitle(_translate("MainWindow", "Log Level"))
        self.menuTabs.setTitle(_translate("MainWindow", "Tabs"))
        self.actionDISABLE.setText(_translate("MainWindow", "DISABLE"))
        self.actionWARNING.setText(_translate("MainWindow", "WARNING"))
        self.actionINFO.setText(_translate("MainWindow", "INFO"))
        self.actionDEBUG.setText(_translate("MainWindow", "DEBUG"))
        self.actionVERBOSE.setText(_translate("MainWindow", "VERBOSE"))
        self.actionToggle_developer_log.setText(_translate("MainWindow", "Toggle Developer Logview"))
        self.actionReset_all_tabs.setText(_translate("MainWindow", "Reset all tabs"))
        self.actionAdd_patron.setText(_translate("MainWindow", "New patron"))
        self.actionRemove_patron.setText(_translate("MainWindow", "Remove patron"))
        self.action_update_tabs_from_file.setText(_translate("MainWindow", "Update Tabs From File"))
        self.action_manually_set_tab.setText(_translate("MainWindow", "Manually set tab"))