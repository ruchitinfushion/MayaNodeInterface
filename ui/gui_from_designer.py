# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_from_designer.ui'
#
# Created: Wed Feb 29 17:21:51 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 859)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainSplitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mainSplitter.sizePolicy().hasHeightForWidth())
        self.mainSplitter.setSizePolicy(sizePolicy)
        self.mainSplitter.setMinimumSize(QtCore.QSize(700, 700))
        self.mainSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.mainSplitter.setChildrenCollapsible(False)
        self.mainSplitter.setObjectName("mainSplitter")
        self.nodeWindow_nodes_Splitter = QtGui.QSplitter(self.mainSplitter)
        self.nodeWindow_nodes_Splitter.setOrientation(QtCore.Qt.Vertical)
        self.nodeWindow_nodes_Splitter.setOpaqueResize(True)
        self.nodeWindow_nodes_Splitter.setChildrenCollapsible(False)
        self.nodeWindow_nodes_Splitter.setObjectName("nodeWindow_nodes_Splitter")
        self.nodeDropGraphicsView = QtGui.QGraphicsView(self.nodeWindow_nodes_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.nodeDropGraphicsView.sizePolicy().hasHeightForWidth())
        self.nodeDropGraphicsView.setSizePolicy(sizePolicy)
        self.nodeDropGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.nodeDropGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.nodeDropGraphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.nodeDropGraphicsView.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
        self.nodeDropGraphicsView.setObjectName("nodeDropGraphicsView")
        self.nodesWindow = QtGui.QTabWidget(self.nodeWindow_nodes_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesWindow.sizePolicy().hasHeightForWidth())
        self.nodesWindow.setSizePolicy(sizePolicy)
        self.nodesWindow.setMinimumSize(QtCore.QSize(450, 209))
        self.nodesWindow.setMovable(True)
        self.nodesWindow.setObjectName("nodesWindow")
        self.conditionsTab = QtGui.QWidget()
        self.conditionsTab.setObjectName("conditionsTab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.conditionsTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.conditionsList = QtGui.QListWidget(self.conditionsTab)
        self.conditionsList.setDragEnabled(True)
        self.conditionsList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.conditionsList.setProperty("isWrapping", True)
        self.conditionsList.setLayoutMode(QtGui.QListView.SinglePass)
        self.conditionsList.setGridSize(QtCore.QSize(100, 20))
        self.conditionsList.setObjectName("conditionsList")
        self.horizontalLayout_4.addWidget(self.conditionsList)
        self.nodesWindow.addTab(self.conditionsTab, "")
        self.nodeOption_description_Splitter = QtGui.QSplitter(self.mainSplitter)
        self.nodeOption_description_Splitter.setOrientation(QtCore.Qt.Vertical)
        self.nodeOption_description_Splitter.setChildrenCollapsible(False)
        self.nodeOption_description_Splitter.setObjectName("nodeOption_description_Splitter")
        self.nodeOptionsWindow = QtGui.QGroupBox(self.nodeOption_description_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nodeOptionsWindow.sizePolicy().hasHeightForWidth())
        self.nodeOptionsWindow.setSizePolicy(sizePolicy)
        self.nodeOptionsWindow.setMinimumSize(QtCore.QSize(225, 200))
        self.nodeOptionsWindow.setObjectName("nodeOptionsWindow")
        self.gridLayout_2 = QtGui.QGridLayout(self.nodeOptionsWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nodeMenuArea = QtGui.QScrollArea(self.nodeOptionsWindow)
        self.nodeMenuArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.nodeMenuArea.setWidgetResizable(True)
        self.nodeMenuArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nodeMenuArea.setObjectName("nodeMenuArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.nodeMenuArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 205, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.nodeMenuArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.nodeMenuArea, 0, 0, 1, 1)
        self.descriptionWindow = QtGui.QGroupBox(self.nodeOption_description_Splitter)
        self.descriptionWindow.setMinimumSize(QtCore.QSize(225, 235))
        self.descriptionWindow.setObjectName("descriptionWindow")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.descriptionWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.descriptionLabel = QtGui.QLabel(self.descriptionWindow)
        self.descriptionLabel.setText("")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.horizontalLayout_2.addWidget(self.descriptionLabel)
        self.gridLayout.addWidget(self.mainSplitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.nodesWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesWindow.setTabText(self.nodesWindow.indexOf(self.conditionsTab), QtGui.QApplication.translate("MainWindow", "Conditional Statements", None, QtGui.QApplication.UnicodeUTF8))
        self.nodeOptionsWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Node Name", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
