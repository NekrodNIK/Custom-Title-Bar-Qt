# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\DJANGO-NIKITA\MoreliaTalk\morelia_client_qt\interfaces\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.CustomTitleBar = QtWidgets.QWidget(self.centralwidget)
        self.CustomTitleBar.setToolTipDuration(-1)
        self.CustomTitleBar.setObjectName("CustomTitleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CustomTitleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(822, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.MinimazeButton = QtWidgets.QPushButton(self.CustomTitleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinimazeButton.sizePolicy().hasHeightForWidth())
        self.MinimazeButton.setSizePolicy(sizePolicy)
        self.MinimazeButton.setMinimumSize(QtCore.QSize(45, 30))
        self.MinimazeButton.setText("")
        self.MinimazeButton.setObjectName("MinimazeButton")
        self.horizontalLayout.addWidget(self.MinimazeButton)
        self.ResizeButton = QtWidgets.QPushButton(self.CustomTitleBar)
        self.ResizeButton.setMinimumSize(QtCore.QSize(45, 30))
        self.ResizeButton.setText("")
        self.ResizeButton.setObjectName("ResizeButton")
        self.horizontalLayout.addWidget(self.ResizeButton)
        self.ExitButton = QtWidgets.QPushButton(self.CustomTitleBar)
        self.ExitButton.setEnabled(True)
        self.ExitButton.setMinimumSize(QtCore.QSize(45, 30))
        self.ExitButton.setText("")
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.gridLayout.addWidget(self.CustomTitleBar, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))