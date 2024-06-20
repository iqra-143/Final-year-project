# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 571)
        MainWindow.setStyleSheet("background-color:rgb(17, 25, 31)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setStyleSheet("color: rgb(245, 245, 245);")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.left_header = QtWidgets.QFrame(self.Header)
        self.left_header.setStyleSheet("color: rgb(187, 198, 206);")
        self.left_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_header.setObjectName("left_header")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.left_header)
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.left_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setMidLineWidth(0)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/source/cam logo 1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.left_header)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("margin: 5px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addWidget(self.left_header)
        self.right_header = QtWidgets.QFrame(self.Header)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.right_header.setFont(font)
        self.right_header.setStyleSheet("QPushButton {\n"
"  margin-right: 10px; /* Adjust the value as needed */\n"
"  padding: 5px 10px; /* Adjust the value as needed */\n"
"}\n"
"")
        self.right_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_header.setObjectName("right_header")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.right_header)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.right_header)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(101, 144, 161);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(90, 128, 143);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(90, 128, 143);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.search_person = QtWidgets.QPushButton(self.right_header)
        self.search_person.setStyleSheet("QPushButton {\n"
"    background-color: rgb(101, 144, 161);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding:10px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(90, 128, 143);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(90, 128, 143);\n"
"}")
        self.search_person.setObjectName("search_person")
        self.horizontalLayout.addWidget(self.search_person)
        self.log = QtWidgets.QPushButton(self.right_header)
        self.log.setStyleSheet("QPushButton {\n"
"    background-color: rgb(101, 144, 161);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding:10px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(90, 128, 143);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(90, 128, 143);\n"
"}")
        self.log.setObjectName("log")
        self.horizontalLayout.addWidget(self.log)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.addWidget(self.right_header)
        self.verticalLayout.addWidget(self.Header, 0, QtCore.Qt.AlignTop)
        self.Main = QtWidgets.QFrame(self.centralwidget)
        self.Main.setStyleSheet("")
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 417, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 3, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.Main)
        self.label_10.setMinimumSize(QtCore.QSize(150, 20))
        self.label_10.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
"color: rgb(225, 230, 235);")
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.Main)
        self.label_11.setMinimumSize(QtCore.QSize(200, 15))
        self.label_11.setMaximumSize(QtCore.QSize(200, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(115, 130, 140);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 425, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.Main)
        self.label_5.setMinimumSize(QtCore.QSize(180, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.Main)
        self.label_12.setMinimumSize(QtCore.QSize(180, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Main)
        self.label_4.setMinimumSize(QtCore.QSize(180, 180))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.Main)
        self.label_8.setMinimumSize(QtCore.QSize(180, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Main)
        self.label_7.setMinimumSize(QtCore.QSize(180, 180))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Main)
        self.label_9.setMinimumSize(QtCore.QSize(180, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"color:rgb(170, 170, 170);\n"
"margin: 5px;\n"
"qproperty-alignment: AlignCenter;\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 2, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(38, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 4, 1, 1)
        self.verticalLayout.addWidget(self.Main)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setStyleSheet("color: rgb(187, 198, 206);")
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_footer_2 = QtWidgets.QFrame(self.footer)
        self.left_footer_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_footer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_footer_2.setObjectName("left_footer_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.left_footer_2)
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.left_footer_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addWidget(self.left_footer_2, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "PERSON REID"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.search_person.setText(_translate("MainWindow", "Search Person"))
        self.log.setText(_translate("MainWindow", "Logout"))
        self.label_10.setText(_translate("MainWindow", "Live Camera Feed"))
        self.label_11.setText(_translate("MainWindow", "Monitor upto 6 cameras for person re-identification "))
        self.label_5.setText(_translate("MainWindow", "Camera 2"))
        self.label_12.setText(_translate("MainWindow", "Camera 3"))
        self.label_4.setText(_translate("MainWindow", "Camera 1"))
        self.label_8.setText(_translate("MainWindow", "Camera 5"))
        self.label_7.setText(_translate("MainWindow", "Camera 4"))
        self.label_9.setText(_translate("MainWindow", "Camera 6"))
        self.label.setText(_translate("MainWindow", "Version 1.0 | Copyright © ReID"))

import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
