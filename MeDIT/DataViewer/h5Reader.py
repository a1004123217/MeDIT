# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h5Reader.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_h5Reader(object):
    def setupUi(self, h5Reader):
        h5Reader.setObjectName("h5Reader")
        h5Reader.resize(954, 728)
        font = QtGui.QFont()
        font.setPointSize(12)
        h5Reader.setFont(font)
        self.centralwidget = QtWidgets.QWidget(h5Reader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree.setObjectName("tree")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree.headerItem().setFont(1, font)
        self.horizontalLayout.addWidget(self.tree)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.matplotWidget = MatplotlibWidget(self.centralwidget)
        self.matplotWidget.setObjectName("matplotWidget")
        self.verticalLayout.addWidget(self.matplotWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        h5Reader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(h5Reader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setMinimumSize(QtCore.QSize(0, 0))
        self.menuFile.setObjectName("menuFile")
        h5Reader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(h5Reader)
        self.statusbar.setObjectName("statusbar")
        h5Reader.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(h5Reader)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(h5Reader)
        QtCore.QMetaObject.connectSlotsByName(h5Reader)

    def retranslateUi(self, h5Reader):
        _translate = QtCore.QCoreApplication.translate
        h5Reader.setWindowTitle(_translate("h5Reader", "MainWindow"))
        self.label.setText(_translate("h5Reader", "FilePath:"))
        self.tree.headerItem().setText(0, _translate("h5Reader", "Key/Tag"))
        self.tree.headerItem().setText(1, _translate("h5Reader", "DataType"))
        self.menuFile.setTitle(_translate("h5Reader", "File"))
        self.actionOpen.setText(_translate("h5Reader", "Open"))

from MatplotlibWidget import MatplotlibWidget
