
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import matplotlib.pyplot as plt
from vectoriel_affiche import *
from ml_affiche import *
from w2v_affiche import *
from content_based_vectoriel import *
from content_based_language import *
from content_based_w2v import *
from neural_hybrid import affiche_list_app2, affiche_tests_app2
from neural_hybrid_rec import affiche_tests_train
from rec_fonction.calcule import *
from rec_fonction.Calcule_hybrid import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1481, 901)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\clap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(173, 173, 201)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1571, 51))
        self.frame.setMinimumSize(QtCore.QSize(1401, 51))
        self.frame.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1480, 0, 71, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(17, 17, 17);\n"
"  color: rgb(255,255,255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(0, 193, 69);\n"
"}")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(580, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(87, 100, 115);")
        self.label_4.setObjectName("label_4")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1410, 50, 70, 46))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(40, 45, 50);\n"
"  color: rgb(255,255,255);\n"
"border: 1px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-exit-to-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1340, 50, 71, 46))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(21, 21, 21);\n"
"  color: rgb(255,255,255);\n"
"border: 1px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 1501, 51))
        self.label.setStyleSheet("background-color: rgb(40, 45, 50);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(141, 141, 141);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
" background-color: rgb(40, 45, 50);\n"
"\n"
" color: rgb(255,255,255);\n"
" border:1px solid;\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-dialpad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"  background-color: rgb(40, 45, 50);\n"
"border:1px solid;\n"
"\n"
" color: rgb(255,255,255);\n"
"\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"   background-color: rgb(40, 45, 50);\n"
"border:1px solid;\n"
"\n"
" color: rgb(255,255,255);\n"
"\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 96, 1491, 781))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.stackedWidget.setObjectName("stackedWidget")



        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(1130, 100, 261, 101))
        self.pushButton_10
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"  background-color: rgb(96, 96, 96);"
"  text-align: center;\n"
"\n"
" color: rgb(0,0,0);\n"
" border:1px solid;\n"
"\n"
"border-radius: 10px;}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")

        self.pushButton_10.setObjectName("pushButton_10")

        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(0, 270, 1501, 21))
        self.line.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 350, 700, 331))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(710, 290, 20, 451))
        self.line_2.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(750, 350, 710, 331))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1491, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(87, 100, 115);\n"
"background-color: rgb(21, 21, 21);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")

        self.line_7 = QtWidgets.QFrame(self.page)
        self.line_7.setGeometry(QtCore.QRect(0, 740, 1501, 20))
        self.line_7.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")


        self.lineEdit_9 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 80, 900, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_10 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 180, 900, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.label_60 = QtWidgets.QLabel(self.page)
        self.label_60.setGeometry(QtCore.QRect(80, 140, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(87, 100, 115);\n"
                                   "background-color: rgb(224, 224, 224);")
        self.label_60.setObjectName("label_60")

        self.label_61 = QtWidgets.QLabel(self.page)
        self.label_61.setGeometry(QtCore.QRect(80, 40, 250, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(87, 100, 115);\n"
                                    "background-color: rgb(224, 224, 224);")
        self.label_61.setObjectName("label_61")

        self.pushButton_45 = QtWidgets.QPushButton(self.page)
        self.pushButton_45.setGeometry(QtCore.QRect(1000, 180, 50, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("QPushButton{\n"
                                         "  background-color: rgb(96, 96, 96);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 10px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_45.setObjectName("pushButton_45")

        self.pushButton_46 = QtWidgets.QPushButton(self.page)
        self.pushButton_46.setGeometry(QtCore.QRect(1000, 80, 50, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("QPushButton{\n"
                                         "  background-color: rgb(96, 96, 96);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 10px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_46.setObjectName("pushButton_46")



        self.label_62 = QtWidgets.QLabel(self.page)
        self.label_62.setGeometry(QtCore.QRect(150, 1040, 250, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(87, 100, 115);\n"
                                    "background-color: rgb(224, 224, 224);")
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.page)
        self.label_63.setGeometry(QtCore.QRect(1000, 800, 50, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(87, 100, 115);\n"
                                    "background-color: rgb(224, 224, 224);")
        self.label_63.setObjectName("label_63")
        data2 = {'1': 9543, '2': 9430, '3': 82155, '4': 90047, '5': 76887}
        x = list(data2.keys())
        y = list(data2.values())
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel('Ratings')
        plt.ylabel('Count')
        plt.bar(x,y, color = 'maroon', width = 0.4)
        plt.title("Les évaluation des utilisateurs dans le dataset d'apprentissage")
        plt.savefig('plt1.png')

        x = list(data2.keys())
        y = list(data2.values())
        fig = plt.figure(figsize=(10, 5))
        plt.xlabel('Ratings')
        plt.ylabel('Count')
        plt.bar(x, y, color='maroon', width=0.4)
        plt.title("Les évaluation des utilisateurs dans le dataset de test")
        plt.savefig('plt2.png')

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_10.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line_2.raise_()
        self.label_5.raise_()
        self.line_7.raise_()
        self.line.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.stackedWidget.addWidget(self.page)



        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(560, 50, 971, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.line_3 = QtWidgets.QFrame(self.page_2)
        self.line_3.setGeometry(QtCore.QRect(610, 60, 11, 721))
        self.line_3.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.page_2)
        self.line_4.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_4.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setObjectName("line_4")

        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_3.setStyleSheet("background-color: rgb(21, 21, 21);")
        "rgb(50, 57, 66)"
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.pushButton_38 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_38.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(192, 192, 192);\n"
                                        "\n"
                                        " color: rgb(0,0,0);\n"
                                        " border:1px solid;\n"
                                        "\n"
                                        " border-bottom-color: rgb(50, 57, 66);\n"
                                        "\n"
                                        "border-radius: 2px;}\n"
                                        "QPushButton:hover{ \n"
                                        "background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.pushButton_38.setObjectName("pushButton_38")

        self.pushButton_39 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_39.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_39.setObjectName("pushButton_39")

        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(0, 51, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.pushButton_11 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_11.setGeometry(QtCore.QRect(380, 550, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("\n"
"QPushButton{\n"
"  background-color: rgb(192, 192, 192);\n"
"\n"
" color: rgb(0,0,0);\n"
" border:1px solid;\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"\n"
"    \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:\\User\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon14)
        self.pushButton_11.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_12.setGeometry(QtCore.QRect(940, 160, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192,192,192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 10px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("C:\\User\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon15)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setObjectName("pushButton_12")

        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(670, 210, 721, 151))
        self.tableWidget.setStyleSheet("QTableWidget { \n"
"    selection-background-color: rgb(100, 100,100);\n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(192, 192, 192);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 10px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 1px;\n"
"    color: rgb(0, 0, 0);\n"
"    PointSize:10;\n"
"    \n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 3px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}")
        self.tableWidget.setRowCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: rgb(192, 192, 192);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(255, 193, 69);\n"
"}")
        self.pushButton_13.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-object-ungroup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon16)
        self.pushButton_13.setObjectName("pushButton_13")

        self.graphicsView = PlotWidget(self.page_2)
        self.graphicsView.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground((96, 96, 96))
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(50, 40))
        self.scrollArea_2.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"border: 0px solid;\n"
"border-radius:5px;\n"
"")
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 480, 301))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_11.sizePolicy().hasHeightForWidth())
        self.textBrowser_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_11.setFont(font)
        self.textBrowser_11.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_11.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"border-radius:5px;\n"
"")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.gridLayout_2.addWidget(self.textBrowser_11, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(850, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 590, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_30 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_30.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_30.setIcon(icon16)
        self.pushButton_30.setObjectName("pushButton_30")

        self.pushButton_31 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_31.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_31.setIcon(icon16)
        self.pushButton_31.setObjectName("pushButton_31")

        self.pushButton_35 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_35.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon17)
        self.pushButton_35.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_35.setObjectName("pushButton_35")

        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(1330, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")

        self.label_47 = QtWidgets.QLabel(self.page_2)
        self.label_47.setGeometry(QtCore.QRect(40, 610, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")

        self.label_50 = QtWidgets.QLabel(self.page_2)
        self.label_50.setGeometry(QtCore.QRect(640, 120, 210, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")

        self.label_51 = QtWidgets.QLabel(self.page_2)
        self.label_51.setGeometry(QtCore.QRect(1180, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_7.raise_()
        self.line_4.raise_()
        self.frame_3.raise_()
        self.label_8.raise_()
        self.line_3.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.tableWidget.raise_()
        self.pushButton_13.raise_()
        self.graphicsView.raise_()
        self.scrollArea_2.raise_()
        self.label_27.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_35.raise_()
        self.lineEdit_13.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_50.raise_()
        self.label_51.raise_()
        self.stackedWidget.addWidget(self.page_2)






        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")

        self.label_100 = QtWidgets.QLabel(self.page_10)
        self.label_100.setGeometry(QtCore.QRect(560, 50, 971, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(192, 192, 192);")
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")

        self.line_100 = QtWidgets.QFrame(self.page_10)
        self.line_100.setGeometry(QtCore.QRect(610, 60, 11, 721))
        self.line_100.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_100.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_100.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_100.setObjectName("line_100")

        self.line_101 = QtWidgets.QFrame(self.page_10)
        self.line_101.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_101.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_101.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_101.setObjectName("line_101")

        self.frame_100 = QtWidgets.QFrame(self.page_10)
        self.frame_100.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_100.setStyleSheet("background-color: rgb(21, 21, 21);")
        "rgb(50, 57, 66)"
        self.frame_100.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_100.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_100.setObjectName("frame_100")

        self.pushButton_100 = QtWidgets.QPushButton(self.frame_100)
        self.pushButton_100.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_100.setObjectName("pushButton_100")

        self.pushButton_101 = QtWidgets.QPushButton(self.frame_100)
        self.pushButton_101.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_101.setFont(font)
        self.pushButton_101.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_101.setObjectName("pushButton_101")

        self.label_101 = QtWidgets.QLabel(self.page_10)
        self.label_101.setGeometry(QtCore.QRect(0, 51, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(192, 192, 192);")
        self.label_101.setAlignment(QtCore.Qt.AlignCenter)
        self.label_101.setObjectName("label_101")

        self.pushButton_102 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_102.setGeometry(QtCore.QRect(380, 520, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "    \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:\\User\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-list.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_102.setIcon(icon14)
        self.pushButton_102.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_102.setObjectName("pushButton_102")

        self.pushButton_103 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_103.setGeometry(QtCore.QRect(940, 160, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192,192,192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 10px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("C:\\User\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-terminal.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_103.setIcon(icon15)
        self.pushButton_103.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_103.setObjectName("pushButton_103")

        self.tableWidget_100 = QtWidgets.QTableWidget(self.page_10)
        self.tableWidget_100.setGeometry(QtCore.QRect(670, 210, 721, 151))
        self.tableWidget_100.setStyleSheet("QTableWidget { \n"
                                       "    selection-background-color: rgb(100, 100,100);\n"
                                       "    font: 9pt \"Segoe UI\";\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background-color: rgb(192, 192, 192);\n"
                                       "    padding: 10px;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "QScrollBar:horizontal {\n"
                                       "    border: none;\n"
                                       "    background: rgb(52, 59, 72);\n"
                                       "    height: 10px;\n"
                                       "    margin: 0px 21px 0 21px;\n"
                                       "    border-radius: 0px;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QHeaderView::section:horizontal\n"
                                       "{\n"
                                       "    background-color: rgb(96, 96, 96);\n"
                                       "    padding: 1px;\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    PointSize:10;\n"
                                       "    \n"
                                       "}\n"
                                       "QHeaderView::section:vertical\n"
                                       "{\n"
                                       "    border: 1px solid rgb(32, 34, 42);\n"
                                       "    background-color: rgb(96, 96, 96);\n"
                                       "    padding: 3px;\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    border-top-left-radius: 0px;\n"
                                       "    border-top-right-radius: 0px;\n"
                                       "}")
        self.tableWidget_100.setRowCount(2)
        self.tableWidget_100.setObjectName("tableWidget_100")
        self.tableWidget_100.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_100.setHorizontalHeaderItem(3, item)

        self.pushButton_104 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_104.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_104.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(192, 192, 192);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(255, 193, 69);\n"
                                         "}")
        self.pushButton_104.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
                QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-object-ungroup.png"),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_104.setIcon(icon16)
        self.pushButton_104.setObjectName("pushButton_104")

        self.graphicsView_100 = PlotWidget(self.page_10)
        self.graphicsView_100.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_100.setObjectName("graphicsView_100")
        self.graphicsView_100.setBackground((96, 96, 96))
        self.scrollArea_100 = QtWidgets.QScrollArea(self.page_10)
        self.scrollArea_100.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_100.setMinimumSize(QtCore.QSize(50, 40))
        self.scrollArea_100.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "border: 0px solid;\n"
                                        "border-radius:5px;\n"
                                        "")
        self.scrollArea_100.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_100.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_100.setWidgetResizable(True)
        self.scrollArea_100.setObjectName("scrollArea_100")
        self.scrollAreaWidgetContents_100 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_100.setGeometry(QtCore.QRect(0, 0, 480, 301))
        self.scrollAreaWidgetContents_100.setObjectName("scrollAreaWidgetContents_100")
        self.gridLayout_100 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_100)
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.textBrowser_100 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_11.sizePolicy().hasHeightForWidth())
        self.textBrowser_100.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_100.setFont(font)
        self.textBrowser_100.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_100.setStyleSheet("background-color: rgb(160, 160, 160);\n"
                                          "border-radius:5px;\n"
                                          "")
        self.textBrowser_100.setObjectName("textBrowser_100")
        self.gridLayout_100.addWidget(self.textBrowser_100, 0, 0, 1, 1)
        self.scrollArea_100.setWidget(self.scrollAreaWidgetContents_100)

        self.label_102 = QtWidgets.QLabel(self.page_10)
        self.label_102.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_102.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_102.setObjectName("label_102")

        self.lineEdit_100 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_100.setGeometry(QtCore.QRect(850, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_100.setFont(font)
        self.lineEdit_100.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 5px;")
        self.lineEdit_100.setObjectName("lineEdit_100")

        self.lineEdit_101 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_101.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_101.setFont(font)
        self.lineEdit_101.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 5px;")
        self.lineEdit_101.setObjectName("lineEdit_101")

        self.pushButton_105 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_105.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_105.setFont(font)
        self.pushButton_105.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_105.setIcon(icon16)
        self.pushButton_105.setObjectName("pushButton_105")

        self.pushButton_106 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_106.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_106.setFont(font)
        self.pushButton_106.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_106.setIcon(icon16)
        self.pushButton_106.setObjectName("pushButton_106")

        self.pushButton_107 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_107.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_107.setFont(font)
        self.pushButton_107.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("C:\\Users\\USER\\PycharmProjects\\Recommender\\icons\\20x20\\cil-remove.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_107.setIcon(icon17)
        self.pushButton_107.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_107.setObjectName("pushButton_107")


        self.label_103 = QtWidgets.QLabel(self.page_10)
        self.label_103.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_103.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_103.setObjectName("label_103")

        self.label_105 = QtWidgets.QLabel(self.page_10)
        self.label_105.setGeometry(QtCore.QRect(640, 120, 210, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_105.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_105.setObjectName("label_105")


        self.label_100.raise_()
        self.line_101.raise_()
        self.frame_100.raise_()
        self.label_101.raise_()
        self.line_100.raise_()
        self.pushButton_102.raise_()
        self.pushButton_103.raise_()
        self.tableWidget_100.raise_()
        self.pushButton_104.raise_()
        self.graphicsView_100.raise_()
        self.scrollArea_2.raise_()
        self.label_102.raise_()
        self.lineEdit_100.raise_()
        self.lineEdit_101.raise_()
        self.pushButton_105.raise_()
        self.pushButton_31.raise_()
        self.pushButton_35.raise_()
        self.label_103.raise_()
        self.label_105.raise_()
        self.stackedWidget.addWidget(self.page_10)







        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.frame_4 = QtWidgets.QFrame(self.page_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_4.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.pushButton_40 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_40.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"                                        
                                         "}")
        self.pushButton_40.setObjectName("pushButton_40")

        self.pushButton_41 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_41.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_41.setObjectName("pushButton_41")

        self.pushButton_42 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_42.setGeometry(QtCore.QRect(278, 22, 140, 31))
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_42.setObjectName("pushButton_42")

        self.pushButton_14 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_14.setGeometry(QtCore.QRect(40, 590, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("\n"
"QPushButton{\n"
"  background-color: rgb(192, 192, 192);\n"
"\n"
" color: rgb(0,0,0);\n"
" border:1px solid;\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"\n"
"    \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")

        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(690, 165, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"selection-color: rgb(255, 170, 0);\n"
"selection-background-color: rgb(85, 170, 0);\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(255,255,255);\n"
" border:0px solid;\n"
"\n"
"border-radius: 10px;")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color: rgb(160,160,160);\n"
"color: rgb(16, 16, 16);\n"
"\n"
"font: 9pt \"Segoe UI\";")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:rgb(160,160,160);\n"
"color: rgb(13, 13, 13);\n"
"font: 9pt \"Segoe UI\";")
        self.radioButton_2.setObjectName("radioButton_2")

        self.groupBox_3 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 510, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                    "selection-color: rgb(255, 170, 0);\n"
                                    "selection-background-color: rgb(85, 170, 0);\n"
                                    "font: 11pt \"Segoe UI\";\n"
                                    "color: rgb(255,255,255);\n"
                                    " border:0px solid;\n"
                                    "\n"
                                    "border-radius: 10px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")

        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("background-color: rgb(160,160,160);\n"
                                       "color: rgb(16, 16, 16);\n"
                                       "\n"
                                       "font: 9pt \"Segoe UI\";")
        self.radioButton_6.setCheckable(True)
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_7.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setStyleSheet("background-color:rgb(160,160,160);\n"
                                         "color: rgb(13, 13, 13);\n"
                                         "font: 9pt \"Segoe UI\";")
        self.radioButton_7.setObjectName("radioButton_7")

        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(0, 50, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(630, 50, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")

        self.pushButton_16 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_16.setGeometry(QtCore.QRect(1110, 164, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192,192,192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")

        self.pushButton_16.setIcon(icon15)
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_17.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    background-color: rgb(192, 192, 192);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(255, 193, 69);\n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon16)
        self.pushButton_17.setObjectName("pushButton_17")

        self.graphicsView_2 = PlotWidget(self.page_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_2.setBackground((96, 96, 96))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.line_5 = QtWidgets.QFrame(self.page_3)
        self.line_5.setGeometry(QtCore.QRect(610, 50, 20, 721))
        self.line_5.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setObjectName("line_5")

        self.line_13 = QtWidgets.QFrame(self.page_3)
        self.line_13.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_13.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_13.setObjectName("line_4")

        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"border: 0px solid;\n"
"border-radius:5px;\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 301))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"border-radius:5px;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_28 = QtWidgets.QLabel(self.page_3)
        self.label_28.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(970, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(670, 210, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("QTableWidget { \n"
"    selection-background-color: rgb(100, 100,100);\n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(192, 192, 192);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 10px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 1px;\n"
"    color: rgb(0, 0, 0);\n"
"    PointSize:10;\n"
"    \n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 3px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}")
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        self.pushButton_32 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_32.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_32.setIcon(icon16)
        self.pushButton_32.setObjectName("pushButton_32")

        self.pushButton_33 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_33.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_33.setIcon(icon16)
        self.pushButton_33.setObjectName("pushButton_33")

        self.pushButton_34 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_34.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_34.setIcon(icon17)
        self.pushButton_34.setObjectName("pushButton_34")

        self.label_48 = QtWidgets.QLabel(self.page_3)
        self.label_48.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")

        self.label_49 = QtWidgets.QLabel(self.page_3)
        self.label_49.setGeometry(QtCore.QRect(690, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")

        self.frame_4.raise_()
        self.pushButton_14.raise_()
        self.groupBox.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton_16.raise_()
        self.graphicsView_2.raise_()
        self.line_5.raise_()
        self.scrollArea.raise_()
        self.label_28.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_17.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.label_48.raise_()
        self.label_49.raise_()
        self.stackedWidget.addWidget(self.page_3)






        self.page_200 = QtWidgets.QWidget()
        self.page_200.setObjectName("page_200")

        self.frame_200 = QtWidgets.QFrame(self.page_200)
        self.frame_200.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_200.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_200.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_200.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_200.setObjectName("frame_200")

        self.pushButton_200 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_200.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.pushButton_200.setFont(font)
        self.pushButton_200.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_200.setObjectName("pushButton_200")

        self.pushButton_201 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_201.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_201.setFont(font)
        self.pushButton_201.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_201.setObjectName("pushButton_201")

        self.pushButton_202 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_202.setGeometry(QtCore.QRect(278, 22, 140, 31))
        self.pushButton_202.setFont(font)
        self.pushButton_202.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_202.setObjectName("pushButton_202")

        self.pushButton_203 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_203.setGeometry(QtCore.QRect(40, 590, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_203.setFont(font)
        self.pushButton_203.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "    \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_203.setObjectName("pushButton_203")

        self.groupBox_200 = QtWidgets.QGroupBox(self.page_200)
        self.groupBox_200.setGeometry(QtCore.QRect(690, 165, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_200.setFont(font)
        self.groupBox_200.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                    "selection-color: rgb(255, 170, 0);\n"
                                    "selection-background-color: rgb(85, 170, 0);\n"
                                    "font: 11pt \"Segoe UI\";\n"
                                    "color: rgb(255,255,255);\n"
                                    " border:0px solid;\n"
                                    "\n"
                                    "border-radius: 10px;")
        self.groupBox_200.setTitle("")
        self.groupBox_200.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_200.setFlat(False)
        self.groupBox_200.setCheckable(False)
        self.groupBox_200.setObjectName("groupBox_200")

        self.radioButton_200 = QtWidgets.QRadioButton(self.groupBox_200)
        self.radioButton_200.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_200.setFont(font)
        self.radioButton_200.setStyleSheet("background-color: rgb(160,160,160);\n"
                                       "color: rgb(16, 16, 16);\n"
                                       "\n"
                                       "font: 9pt \"Segoe UI\";")
        self.radioButton_200.setCheckable(True)
        self.radioButton_200.setChecked(False)
        self.radioButton_200.setObjectName("radioButton_200")

        self.radioButton_201 = QtWidgets.QRadioButton(self.groupBox_200)
        self.radioButton_201.setGeometry(QtCore.QRect(200, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_201.setFont(font)
        self.radioButton_201.setStyleSheet("background-color:rgb(160,160,160);\n"
                                         "color: rgb(13, 13, 13);\n"
                                         "font: 9pt \"Segoe UI\";")
        self.radioButton_201.setObjectName("radioButton_201")

        self.groupBox_201 = QtWidgets.QGroupBox(self.page_200)
        self.groupBox_201.setGeometry(QtCore.QRect(400, 510, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_201.setFont(font)
        self.groupBox_201.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                      "selection-color: rgb(255, 170, 0);\n"
                                      "selection-background-color: rgb(85, 170, 0);\n"
                                      "font: 11pt \"Segoe UI\";\n"
                                      "color: rgb(255,255,255);\n"
                                      " border:0px solid;\n"
                                      "\n"
                                      "border-radius: 10px;")
        self.groupBox_201.setTitle("")
        self.groupBox_201.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_201.setFlat(False)
        self.groupBox_201.setCheckable(False)
        self.groupBox_201.setObjectName("groupBox_201")

        self.radioButton_202 = QtWidgets.QRadioButton(self.groupBox_201)
        self.radioButton_202.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_202.setFont(font)
        self.radioButton_202.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "\n"
                                         "font: 9pt \"Segoe UI\";")
        self.radioButton_202.setCheckable(True)
        self.radioButton_202.setChecked(False)
        self.radioButton_202.setObjectName("radioButton_202")

        self.radioButton_203 = QtWidgets.QRadioButton(self.groupBox_201)
        self.radioButton_203.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_203.setFont(font)
        self.radioButton_203.setStyleSheet("background-color:rgb(160,160,160);\n"
                                         "color: rgb(13, 13, 13);\n"
                                         "font: 9pt \"Segoe UI\";")
        self.radioButton_203.setObjectName("radioButton_203")

        self.label_200 = QtWidgets.QLabel(self.page_200)
        self.label_200.setGeometry(QtCore.QRect(0, 50, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_200.setFont(font)
        self.label_200.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(192, 192, 192);")
        self.label_200.setAlignment(QtCore.Qt.AlignCenter)
        self.label_200.setObjectName("label_200")

        self.label_201 = QtWidgets.QLabel(self.page_200)
        self.label_201.setGeometry(QtCore.QRect(630, 50, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_201.setFont(font)
        self.label_201.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(192, 192, 192);")
        self.label_201.setAlignment(QtCore.Qt.AlignCenter)
        self.label_201.setObjectName("label_201")

        self.pushButton_204 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_204.setGeometry(QtCore.QRect(1110, 164, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_204.setFont(font)
        self.pushButton_204.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192,192,192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")

        self.pushButton_204.setIcon(icon15)
        self.pushButton_204.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_204.setObjectName("pushButton_204")

        self.pushButton_205 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_205.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_205.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(192, 192, 192);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(255, 193, 69);\n"
                                         "}")
        self.pushButton_205.setText("")
        self.pushButton_205.setIcon(icon16)
        self.pushButton_205.setObjectName("pushButton_205")

        self.graphicsView_200 = PlotWidget(self.page_200)
        self.graphicsView_200.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_200.setBackground((96, 96, 96))
        self.graphicsView_200.setObjectName("graphicsView_200")

        self.line_200 = QtWidgets.QFrame(self.page_200)
        self.line_200.setGeometry(QtCore.QRect(610, 50, 20, 721))
        self.line_200.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_200.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_200.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_200.setObjectName("line_200")

        self.line_201 = QtWidgets.QFrame(self.page_200)
        self.line_201.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_201.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_201.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_201.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_201.setObjectName("line_201")

        self.scrollArea_200 = QtWidgets.QScrollArea(self.page_200)
        self.scrollArea_200.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_200.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea_200.setFont(font)
        self.scrollArea_200.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                      "border: 0px solid;\n"
                                      "border-radius:5px;\n"
                                      "")
        self.scrollArea_200.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_200.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_200.setWidgetResizable(True)
        self.scrollArea_200.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_200 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_200.setGeometry(QtCore.QRect(0, 0, 400, 301))
        self.scrollAreaWidgetContents_200.setObjectName("scrollAreaWidgetContents_200")
        self.gridLayout_200 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_200)
        self.gridLayout_200.setObjectName("gridLayout_200")
        self.textBrowser_200 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_200.sizePolicy().hasHeightForWidth())
        self.textBrowser_200.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser_200.setFont(font)
        self.textBrowser_200.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_200.setStyleSheet("background-color: rgb(160, 160, 160);\n"
                                       "border-radius:5px;\n"
                                       "")
        self.textBrowser_200.setObjectName("textBrowser_200")
        self.gridLayout_200.addWidget(self.textBrowser_200, 0, 0, 1, 1)
        self.scrollArea_200.setWidget(self.scrollAreaWidgetContents_200)

        self.label_202 = QtWidgets.QLabel(self.page_200)
        self.label_202.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_202.setFont(font)
        self.label_202.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_202.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_202.setObjectName("label_202")

        self.lineEdit_200 = QtWidgets.QLineEdit(self.page_200)
        self.lineEdit_200.setGeometry(QtCore.QRect(970, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_200.setFont(font)
        self.lineEdit_200.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 5px;")
        self.lineEdit_200.setObjectName("lineEdit_200")

        self.lineEdit_201 = QtWidgets.QLineEdit(self.page_200)
        self.lineEdit_201.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_201.setFont(font)
        self.lineEdit_201.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                      "border: 1px solid;\n"
                                      "border-radius: 5px;")
        self.lineEdit_201.setObjectName("lineEdit_201")

        self.tableWidget_200 = QtWidgets.QTableWidget(self.page_200)
        self.tableWidget_200.setGeometry(QtCore.QRect(670, 210, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_200.setFont(font)
        self.tableWidget_200.setStyleSheet("QTableWidget { \n"
                                         "    selection-background-color: rgb(100, 100,100);\n"
                                         "    font: 9pt \"Segoe UI\";\n"
                                         "    color: rgb(0, 0, 0);\n"
                                         "    background-color: rgb(192, 192, 192);\n"
                                         "    padding: 10px;\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QScrollBar:horizontal {\n"
                                         "    border: none;\n"
                                         "    background: rgb(52, 59, 72);\n"
                                         "    height: 10px;\n"
                                         "    margin: 0px 21px 0 21px;\n"
                                         "    border-radius: 0px;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QHeaderView::section:horizontal\n"
                                         "{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "    padding: 1px;\n"
                                         "    color: rgb(0, 0, 0);\n"
                                         "    PointSize:10;\n"
                                         "    \n"
                                         "}\n"
                                         "QHeaderView::section:vertical\n"
                                         "{\n"
                                         "    border: 1px solid rgb(32, 34, 42);\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "    padding: 3px;\n"
                                         "    color: rgb(0, 0, 0);\n"
                                         "    border-top-left-radius: 0px;\n"
                                         "    border-top-right-radius: 0px;\n"
                                         "}")
        self.tableWidget_200.setRowCount(2)
        self.tableWidget_200.setObjectName("tableWidget_200")
        self.tableWidget_200.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(3, item)

        self.pushButton_206 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_206.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_206.setFont(font)
        self.pushButton_206.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_206.setIcon(icon16)
        self.pushButton_206.setObjectName("pushButton_206")

        self.pushButton_207 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_207.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_207.setFont(font)
        self.pushButton_207.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_207.setIcon(icon16)
        self.pushButton_207.setObjectName("pushButton_207")

        self.pushButton_208 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_208.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_208.setFont(font)
        self.pushButton_208.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "  color: rgb(0,0,0);\n"
                                         "border: 0px solid;\n"
                                         "border-radius: 0px;\n"
                                         "}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_208.setIcon(icon17)
        self.pushButton_208.setObjectName("pushButton_208")

        self.label_203 = QtWidgets.QLabel(self.page_200)
        self.label_203.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_203.setFont(font)
        self.label_203.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_203.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_203.setObjectName("label_203")

        self.label_204 = QtWidgets.QLabel(self.page_200)
        self.label_204.setGeometry(QtCore.QRect(690, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_204.setFont(font)
        self.label_204.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_204.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_204.setObjectName("label_204")

        self.frame_200.raise_()
        self.pushButton_203.raise_()
        self.groupBox_200.raise_()
        self.label_200.raise_()
        self.label_201.raise_()
        self.pushButton_204.raise_()
        self.graphicsView_200.raise_()
        self.line_200.raise_()
        self.scrollArea_200.raise_()
        self.label_202.raise_()
        self.lineEdit_200.raise_()
        self.lineEdit_201.raise_()
        self.tableWidget_200.raise_()
        self.pushButton_205.raise_()
        self.pushButton_206.raise_()
        self.pushButton_207.raise_()
        self.pushButton_208.raise_()
        self.label_203.raise_()
        self.label_204.raise_()
        self.stackedWidget.addWidget(self.page_200)

        self.page_200 = QtWidgets.QWidget()
        self.page_200.setObjectName("page_200")

        self.frame_200 = QtWidgets.QFrame(self.page_200)
        self.frame_200.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_200.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_200.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_200.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_200.setObjectName("frame_200")

        self.pushButton_200 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_200.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.pushButton_200.setFont(font)
        self.pushButton_200.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(160, 160, 160);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_200.setObjectName("pushButton_200")

        self.pushButton_201 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_201.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_201.setFont(font)
        self.pushButton_201.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(192, 192, 192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_201.setObjectName("pushButton_201")

        self.pushButton_202 = QtWidgets.QPushButton(self.frame_200)
        self.pushButton_202.setGeometry(QtCore.QRect(278, 22, 140, 31))
        self.pushButton_202.setFont(font)
        self.pushButton_202.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(160, 160, 160);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_202.setObjectName("pushButton_202")

        self.pushButton_203 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_203.setGeometry(QtCore.QRect(40, 590, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_203.setFont(font)
        self.pushButton_203.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192, 192, 192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "    \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_203.setObjectName("pushButton_203")

        self.groupBox_200 = QtWidgets.QGroupBox(self.page_200)
        self.groupBox_200.setGeometry(QtCore.QRect(690, 165, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_200.setFont(font)
        self.groupBox_200.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "selection-color: rgb(255, 170, 0);\n"
                                        "selection-background-color: rgb(85, 170, 0);\n"
                                        "font: 11pt \"Segoe UI\";\n"
                                        "color: rgb(255,255,255);\n"
                                        " border:0px solid;\n"
                                        "\n"
                                        "border-radius: 10px;")
        self.groupBox_200.setTitle("")
        self.groupBox_200.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_200.setFlat(False)
        self.groupBox_200.setCheckable(False)
        self.groupBox_200.setObjectName("groupBox_200")

        self.radioButton_200 = QtWidgets.QRadioButton(self.groupBox_200)
        self.radioButton_200.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_200.setFont(font)
        self.radioButton_200.setStyleSheet("background-color: rgb(160,160,160);\n"
                                           "color: rgb(16, 16, 16);\n"
                                           "\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_200.setCheckable(True)
        self.radioButton_200.setChecked(False)
        self.radioButton_200.setObjectName("radioButton_200")

        self.radioButton_201 = QtWidgets.QRadioButton(self.groupBox_200)
        self.radioButton_201.setGeometry(QtCore.QRect(200, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_201.setFont(font)
        self.radioButton_201.setStyleSheet("background-color:rgb(160,160,160);\n"
                                           "color: rgb(13, 13, 13);\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_201.setObjectName("radioButton_201")

        self.groupBox_201 = QtWidgets.QGroupBox(self.page_200)
        self.groupBox_201.setGeometry(QtCore.QRect(400, 510, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_201.setFont(font)
        self.groupBox_201.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "selection-color: rgb(255, 170, 0);\n"
                                        "selection-background-color: rgb(85, 170, 0);\n"
                                        "font: 11pt \"Segoe UI\";\n"
                                        "color: rgb(255,255,255);\n"
                                        " border:0px solid;\n"
                                        "\n"
                                        "border-radius: 10px;")
        self.groupBox_201.setTitle("")
        self.groupBox_201.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_201.setFlat(False)
        self.groupBox_201.setCheckable(False)
        self.groupBox_201.setObjectName("groupBox_201")

        self.radioButton_202 = QtWidgets.QRadioButton(self.groupBox_201)
        self.radioButton_202.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_202.setFont(font)
        self.radioButton_202.setStyleSheet("background-color: rgb(160,160,160);\n"
                                           "color: rgb(16, 16, 16);\n"
                                           "\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_202.setCheckable(True)
        self.radioButton_202.setChecked(False)
        self.radioButton_202.setObjectName("radioButton_202")

        self.radioButton_203 = QtWidgets.QRadioButton(self.groupBox_201)
        self.radioButton_203.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_203.setFont(font)
        self.radioButton_203.setStyleSheet("background-color:rgb(160,160,160);\n"
                                           "color: rgb(13, 13, 13);\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_203.setObjectName("radioButton_203")

        self.label_200 = QtWidgets.QLabel(self.page_200)
        self.label_200.setGeometry(QtCore.QRect(0, 50, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_200.setFont(font)
        self.label_200.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_200.setAlignment(QtCore.Qt.AlignCenter)
        self.label_200.setObjectName("label_200")

        self.label_201 = QtWidgets.QLabel(self.page_200)
        self.label_201.setGeometry(QtCore.QRect(630, 50, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_201.setFont(font)
        self.label_201.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_201.setAlignment(QtCore.Qt.AlignCenter)
        self.label_201.setObjectName("label_201")

        self.pushButton_204 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_204.setGeometry(QtCore.QRect(1110, 164, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_204.setFont(font)
        self.pushButton_204.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192,192,192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")

        self.pushButton_204.setIcon(icon15)
        self.pushButton_204.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_204.setObjectName("pushButton_204")

        self.pushButton_205 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_205.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_205.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(192, 192, 192);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(255, 193, 69);\n"
                                          "}")
        self.pushButton_205.setText("")
        self.pushButton_205.setIcon(icon16)
        self.pushButton_205.setObjectName("pushButton_205")

        self.graphicsView_200 = PlotWidget(self.page_200)
        self.graphicsView_200.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_200.setBackground((96, 96, 96))
        self.graphicsView_200.setObjectName("graphicsView_200")

        self.line_200 = QtWidgets.QFrame(self.page_200)
        self.line_200.setGeometry(QtCore.QRect(610, 50, 20, 721))
        self.line_200.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_200.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_200.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_200.setObjectName("line_200")

        self.line_201 = QtWidgets.QFrame(self.page_200)
        self.line_201.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_201.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_201.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_201.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_201.setObjectName("line_201")

        self.scrollArea_200 = QtWidgets.QScrollArea(self.page_200)
        self.scrollArea_200.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_200.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea_200.setFont(font)
        self.scrollArea_200.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                          "border: 0px solid;\n"
                                          "border-radius:5px;\n"
                                          "")
        self.scrollArea_200.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_200.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_200.setWidgetResizable(True)
        self.scrollArea_200.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_200 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_200.setGeometry(QtCore.QRect(0, 0, 400, 301))
        self.scrollAreaWidgetContents_200.setObjectName("scrollAreaWidgetContents_200")
        self.gridLayout_200 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_200)
        self.gridLayout_200.setObjectName("gridLayout_200")
        self.textBrowser_200 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_200.sizePolicy().hasHeightForWidth())
        self.textBrowser_200.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser_200.setFont(font)
        self.textBrowser_200.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_200.setStyleSheet("background-color: rgb(160, 160, 160);\n"
                                           "border-radius:5px;\n"
                                           "")
        self.textBrowser_200.setObjectName("textBrowser_200")
        self.gridLayout_200.addWidget(self.textBrowser_200, 0, 0, 1, 1)
        self.scrollArea_200.setWidget(self.scrollAreaWidgetContents_200)

        self.label_202 = QtWidgets.QLabel(self.page_200)
        self.label_202.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_202.setFont(font)
        self.label_202.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_202.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_202.setObjectName("label_202")

        self.lineEdit_200 = QtWidgets.QLineEdit(self.page_200)
        self.lineEdit_200.setGeometry(QtCore.QRect(970, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_200.setFont(font)
        self.lineEdit_200.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_200.setObjectName("lineEdit_200")

        self.lineEdit_201 = QtWidgets.QLineEdit(self.page_200)
        self.lineEdit_201.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_201.setFont(font)
        self.lineEdit_201.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_201.setObjectName("lineEdit_201")

        self.tableWidget_200 = QtWidgets.QTableWidget(self.page_200)
        self.tableWidget_200.setGeometry(QtCore.QRect(670, 210, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_200.setFont(font)
        self.tableWidget_200.setStyleSheet("QTableWidget { \n"
                                           "    selection-background-color: rgb(100, 100,100);\n"
                                           "    font: 9pt \"Segoe UI\";\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    background-color: rgb(192, 192, 192);\n"
                                           "    padding: 10px;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "QScrollBar:horizontal {\n"
                                           "    border: none;\n"
                                           "    background: rgb(52, 59, 72);\n"
                                           "    height: 10px;\n"
                                           "    margin: 0px 21px 0 21px;\n"
                                           "    border-radius: 0px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QHeaderView::section:horizontal\n"
                                           "{\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 1px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    PointSize:10;\n"
                                           "    \n"
                                           "}\n"
                                           "QHeaderView::section:vertical\n"
                                           "{\n"
                                           "    border: 1px solid rgb(32, 34, 42);\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 3px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border-top-left-radius: 0px;\n"
                                           "    border-top-right-radius: 0px;\n"
                                           "}")
        self.tableWidget_200.setRowCount(2)
        self.tableWidget_200.setObjectName("tableWidget_200")
        self.tableWidget_200.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_200.setHorizontalHeaderItem(3, item)

        self.pushButton_206 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_206.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_206.setFont(font)
        self.pushButton_206.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_206.setIcon(icon16)
        self.pushButton_206.setObjectName("pushButton_206")

        self.pushButton_207 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_207.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_207.setFont(font)
        self.pushButton_207.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_207.setIcon(icon16)
        self.pushButton_207.setObjectName("pushButton_207")

        self.pushButton_208 = QtWidgets.QPushButton(self.page_200)
        self.pushButton_208.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_208.setFont(font)
        self.pushButton_208.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_208.setIcon(icon17)
        self.pushButton_208.setObjectName("pushButton_208")

        self.label_203 = QtWidgets.QLabel(self.page_200)
        self.label_203.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_203.setFont(font)
        self.label_203.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_203.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_203.setObjectName("label_203")

        self.label_204 = QtWidgets.QLabel(self.page_200)
        self.label_204.setGeometry(QtCore.QRect(690, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_204.setFont(font)
        self.label_204.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_204.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_204.setObjectName("label_204")

        self.frame_200.raise_()
        self.pushButton_203.raise_()
        self.groupBox_200.raise_()
        self.label_200.raise_()
        self.label_201.raise_()
        self.pushButton_204.raise_()
        self.graphicsView_200.raise_()
        self.line_200.raise_()
        self.scrollArea_200.raise_()
        self.label_202.raise_()
        self.lineEdit_200.raise_()
        self.lineEdit_201.raise_()
        self.tableWidget_200.raise_()
        self.pushButton_205.raise_()
        self.pushButton_206.raise_()
        self.pushButton_207.raise_()
        self.pushButton_208.raise_()
        self.label_203.raise_()
        self.label_204.raise_()
        self.stackedWidget.addWidget(self.page_200)






        self.page_300 = QtWidgets.QWidget()
        self.page_300.setObjectName("page_300")

        self.frame_300 = QtWidgets.QFrame(self.page_300)
        self.frame_300.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_300.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_300.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_300.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_300.setObjectName("frame_300")

        self.pushButton_300 = QtWidgets.QPushButton(self.frame_300)
        self.pushButton_300.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.pushButton_300.setFont(font)
        self.pushButton_300.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(160, 160, 160);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_300.setObjectName("pushButton_300")

        self.pushButton_301 = QtWidgets.QPushButton(self.frame_300)
        self.pushButton_301.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_301.setFont(font)
        self.pushButton_301.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(160, 160, 160);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_301.setObjectName("pushButton_301")

        self.pushButton_302 = QtWidgets.QPushButton(self.frame_300)
        self.pushButton_302.setGeometry(QtCore.QRect(278, 22, 140, 31))
        self.pushButton_302.setFont(font)
        self.pushButton_302.setStyleSheet("QPushButton{\n"
                                          " background-color: rgb(192, 192, 192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border-bottom-color: rgb(50, 57, 66);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 2px;}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_302.setObjectName("pushButton_302")

        self.pushButton_303 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_303.setGeometry(QtCore.QRect(40, 590, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_303.setFont(font)
        self.pushButton_303.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192, 192, 192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "    \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_303.setObjectName("pushButton_303")

        self.groupBox_300 = QtWidgets.QGroupBox(self.page_300)
        self.groupBox_300.setGeometry(QtCore.QRect(690, 165, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_300.setFont(font)
        self.groupBox_300.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "selection-color: rgb(255, 170, 0);\n"
                                        "selection-background-color: rgb(85, 170, 0);\n"
                                        "font: 11pt \"Segoe UI\";\n"
                                        "color: rgb(255,255,255);\n"
                                        " border:0px solid;\n"
                                        "\n"
                                        "border-radius: 10px;")
        self.groupBox_300.setTitle("")
        self.groupBox_300.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_300.setFlat(False)
        self.groupBox_300.setCheckable(False)
        self.groupBox_300.setObjectName("groupBox_300")

        self.radioButton_300 = QtWidgets.QRadioButton(self.groupBox_300)
        self.radioButton_300.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_300.setFont(font)
        self.radioButton_300.setStyleSheet("background-color: rgb(160,160,160);\n"
                                           "color: rgb(16, 16, 16);\n"
                                           "\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_300.setCheckable(True)
        self.radioButton_300.setChecked(False)
        self.radioButton_300.setObjectName("radioButton_300")

        self.radioButton_301 = QtWidgets.QRadioButton(self.groupBox_300)
        self.radioButton_301.setGeometry(QtCore.QRect(200, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_301.setFont(font)
        self.radioButton_301.setStyleSheet("background-color:rgb(160,160,160);\n"
                                           "color: rgb(13, 13, 13);\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_301.setObjectName("radioButton_301")

        self.groupBox_301 = QtWidgets.QGroupBox(self.page_300)
        self.groupBox_301.setGeometry(QtCore.QRect(400, 510, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_301.setFont(font)
        self.groupBox_301.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "selection-color: rgb(255, 170, 0);\n"
                                        "selection-background-color: rgb(85, 170, 0);\n"
                                        "font: 11pt \"Segoe UI\";\n"
                                        "color: rgb(255,255,255);\n"
                                        " border:0px solid;\n"
                                        "\n"
                                        "border-radius: 10px;")
        self.groupBox_301.setTitle("")
        self.groupBox_301.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_301.setFlat(False)
        self.groupBox_301.setCheckable(False)
        self.groupBox_301.setObjectName("groupBox_301")

        self.radioButton_302 = QtWidgets.QRadioButton(self.groupBox_301)
        self.radioButton_302.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_302.setFont(font)
        self.radioButton_302.setStyleSheet("background-color: rgb(160,160,160);\n"
                                           "color: rgb(16, 16, 16);\n"
                                           "\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_302.setCheckable(True)
        self.radioButton_302.setChecked(False)
        self.radioButton_302.setObjectName("radioButton_302")

        self.radioButton_303 = QtWidgets.QRadioButton(self.groupBox_301)
        self.radioButton_303.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_303.setFont(font)
        self.radioButton_303.setStyleSheet("background-color:rgb(160,160,160);\n"
                                           "color: rgb(13, 13, 13);\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_303.setObjectName("radioButton_303")

        self.label_300 = QtWidgets.QLabel(self.page_300)
        self.label_300.setGeometry(QtCore.QRect(0, 50, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_300.setFont(font)
        self.label_300.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_300.setAlignment(QtCore.Qt.AlignCenter)
        self.label_300.setObjectName("label_300")

        self.label_301 = QtWidgets.QLabel(self.page_300)
        self.label_301.setGeometry(QtCore.QRect(630, 50, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_301.setFont(font)
        self.label_301.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_301.setAlignment(QtCore.Qt.AlignCenter)
        self.label_301.setObjectName("label_301")

        self.pushButton_304 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_304.setGeometry(QtCore.QRect(1110, 164, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_304.setFont(font)
        self.pushButton_304.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192,192,192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")

        self.pushButton_304.setIcon(icon15)
        self.pushButton_304.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_304.setObjectName("pushButton_304")

        self.pushButton_305 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_305.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_305.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(192, 192, 192);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(255, 193, 69);\n"
                                          "}")
        self.pushButton_305.setText("")
        self.pushButton_305.setIcon(icon16)
        self.pushButton_305.setObjectName("pushButton_305")

        self.graphicsView_300 = PlotWidget(self.page_300)
        self.graphicsView_300.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_300.setBackground((96, 96, 96))
        self.graphicsView_300.setObjectName("graphicsView_300")

        self.line_300 = QtWidgets.QFrame(self.page_300)
        self.line_300.setGeometry(QtCore.QRect(610, 50, 20, 721))
        self.line_300.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_300.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_300.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_300.setObjectName("line_300")

        self.line_301 = QtWidgets.QFrame(self.page_300)
        self.line_301.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_301.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_301.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_301.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_301.setObjectName("line_301")

        self.scrollArea_300 = QtWidgets.QScrollArea(self.page_300)
        self.scrollArea_300.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_300.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea_300.setFont(font)
        self.scrollArea_300.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                          "border: 0px solid;\n"
                                          "border-radius:5px;\n"
                                          "")
        self.scrollArea_300.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_300.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_300.setWidgetResizable(True)
        self.scrollArea_300.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_300 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_300.setGeometry(QtCore.QRect(0, 0, 400, 301))
        self.scrollAreaWidgetContents_300.setObjectName("scrollAreaWidgetContents_300")
        self.gridLayout_300 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_300)
        self.gridLayout_300.setObjectName("gridLayout_300")
        self.textBrowser_300 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_300.sizePolicy().hasHeightForWidth())
        self.textBrowser_300.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser_300.setFont(font)
        self.textBrowser_300.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_300.setStyleSheet("background-color: rgb(160, 160, 160);\n"
                                           "border-radius:5px;\n"
                                           "")
        self.textBrowser_300.setObjectName("textBrowser_300")
        self.gridLayout_300.addWidget(self.textBrowser_300, 0, 0, 1, 1)
        self.scrollArea_300.setWidget(self.scrollAreaWidgetContents_300)

        self.label_302 = QtWidgets.QLabel(self.page_300)
        self.label_302.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_302.setFont(font)
        self.label_302.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_302.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_302.setObjectName("label_302")

        self.lineEdit_300 = QtWidgets.QLineEdit(self.page_300)
        self.lineEdit_300.setGeometry(QtCore.QRect(970, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_300.setFont(font)
        self.lineEdit_300.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_300.setObjectName("lineEdit_300")

        self.lineEdit_301 = QtWidgets.QLineEdit(self.page_300)
        self.lineEdit_301.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_301.setFont(font)
        self.lineEdit_301.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_301.setObjectName("lineEdit_301")

        self.tableWidget_300 = QtWidgets.QTableWidget(self.page_300)
        self.tableWidget_300.setGeometry(QtCore.QRect(670, 210, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_300.setFont(font)
        self.tableWidget_300.setStyleSheet("QTableWidget { \n"
                                           "    selection-background-color: rgb(100, 100,100);\n"
                                           "    font: 9pt \"Segoe UI\";\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    background-color: rgb(192, 192, 192);\n"
                                           "    padding: 10px;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "QScrollBar:horizontal {\n"
                                           "    border: none;\n"
                                           "    background: rgb(52, 59, 72);\n"
                                           "    height: 10px;\n"
                                           "    margin: 0px 21px 0 21px;\n"
                                           "    border-radius: 0px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QHeaderView::section:horizontal\n"
                                           "{\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 1px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    PointSize:10;\n"
                                           "    \n"
                                           "}\n"
                                           "QHeaderView::section:vertical\n"
                                           "{\n"
                                           "    border: 1px solid rgb(32, 34, 42);\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 3px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border-top-left-radius: 0px;\n"
                                           "    border-top-right-radius: 0px;\n"
                                           "}")
        self.tableWidget_300.setRowCount(2)
        self.tableWidget_300.setObjectName("tableWidget_300")
        self.tableWidget_300.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_300.setHorizontalHeaderItem(3, item)

        self.pushButton_306 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_306.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_306.setFont(font)
        self.pushButton_306.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_306.setIcon(icon16)
        self.pushButton_306.setObjectName("pushButton_306")

        self.pushButton_307 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_307.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_307.setFont(font)
        self.pushButton_307.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_307.setIcon(icon16)
        self.pushButton_307.setObjectName("pushButton_307")

        self.pushButton_308 = QtWidgets.QPushButton(self.page_300)
        self.pushButton_308.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_308.setFont(font)
        self.pushButton_308.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_308.setIcon(icon17)
        self.pushButton_308.setObjectName("pushButton_308")

        self.label_303 = QtWidgets.QLabel(self.page_300)
        self.label_303.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_303.setFont(font)
        self.label_303.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_303.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_303.setObjectName("label_303")

        self.label_304 = QtWidgets.QLabel(self.page_300)
        self.label_304.setGeometry(QtCore.QRect(690, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_304.setFont(font)
        self.label_304.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_304.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_304.setObjectName("label_304")

        self.frame_300.raise_()
        self.pushButton_303.raise_()
        self.groupBox_300.raise_()
        self.label_300.raise_()
        self.label_301.raise_()
        self.pushButton_304.raise_()
        self.graphicsView_300.raise_()
        self.line_300.raise_()
        self.scrollArea_300.raise_()
        self.label_302.raise_()
        self.lineEdit_300.raise_()
        self.lineEdit_301.raise_()
        self.tableWidget_300.raise_()
        self.pushButton_305.raise_()
        self.pushButton_306.raise_()
        self.pushButton_307.raise_()
        self.pushButton_308.raise_()
        self.label_303.raise_()
        self.label_304.raise_()
        self.stackedWidget.addWidget(self.page_300)




        self.page_400 = QtWidgets.QWidget()
        self.page_400.setObjectName("page_400")

        self.frame_400 = QtWidgets.QFrame(self.page_400)
        self.frame_400.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_400.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_400.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_400.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_400.setObjectName("frame_400")

        self.pushButton_400 = QtWidgets.QPushButton(self.frame_400)
        self.pushButton_400.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_400.setFont(font)
        self.pushButton_400.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_400.setObjectName("pushButton_400")

        self.pushButton_401 = QtWidgets.QPushButton(self.frame_400)
        self.pushButton_401.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_401.setFont(font)
        self.pushButton_401.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_401.setObjectName("pushButton_401")

        self.pushButton_403 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_403.setGeometry(QtCore.QRect(400, 510, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_403.setFont(font)
        self.pushButton_403.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192, 192, 192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "    \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_403.setObjectName("pushButton_403")

        self.groupBox_400 = QtWidgets.QGroupBox(self.page_400)
        self.groupBox_400.setGeometry(QtCore.QRect(690, 165, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_400.setFont(font)
        self.groupBox_400.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                        "selection-color: rgb(255, 170, 0);\n"
                                        "selection-background-color: rgb(85, 170, 0);\n"
                                        "font: 11pt \"Segoe UI\";\n"
                                        "color: rgb(255,255,255);\n"
                                        " border:0px solid;\n"
                                        "\n"
                                        "border-radius: 10px;")
        self.groupBox_400.setTitle("")
        self.groupBox_400.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_400.setFlat(False)
        self.groupBox_400.setCheckable(False)
        self.groupBox_400.setObjectName("groupBox_400")

        self.radioButton_400 = QtWidgets.QRadioButton(self.groupBox_400)
        self.radioButton_400.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_400.setFont(font)
        self.radioButton_400.setStyleSheet("background-color: rgb(160,160,160);\n"
                                           "color: rgb(16, 16, 16);\n"
                                           "\n"
                                           "font: 9pt \"Segoe UI\";")
        self.radioButton_400.setCheckable(True)
        self.radioButton_400.setChecked(False)
        self.radioButton_400.setObjectName("radioButton_400")

        self.label_400 = QtWidgets.QLabel(self.page_400)
        self.label_400.setGeometry(QtCore.QRect(0, 50, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_400.setFont(font)
        self.label_400.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_400.setAlignment(QtCore.Qt.AlignCenter)
        self.label_400.setObjectName("label_400")

        self.label_401 = QtWidgets.QLabel(self.page_400)
        self.label_401.setGeometry(QtCore.QRect(630, 50, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_401.setFont(font)
        self.label_401.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(192, 192, 192);")
        self.label_401.setAlignment(QtCore.Qt.AlignCenter)
        self.label_401.setObjectName("label_401")

        self.pushButton_404 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_404.setGeometry(QtCore.QRect(1110, 164, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_404.setFont(font)
        self.pushButton_404.setStyleSheet("\n"
                                          "QPushButton{\n"
                                          "  background-color: rgb(192,192,192);\n"
                                          "\n"
                                          " color: rgb(0,0,0);\n"
                                          " border:1px solid;\n"
                                          "\n"
                                          "border-radius: 5px;}\n"
                                          "QPushButton:hover{ \n"
                                          "\n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")

        self.pushButton_404.setIcon(icon15)
        self.pushButton_404.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_404.setObjectName("pushButton_404")

        self.pushButton_405 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_405.setGeometry(QtCore.QRect(680, 220, 101, 43))
        self.pushButton_405.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(192, 192, 192);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(255, 193, 69);\n"
                                          "}")
        self.pushButton_405.setText("")
        self.pushButton_405.setIcon(icon16)
        self.pushButton_405.setObjectName("pushButton_405")

        self.graphicsView_400 = PlotWidget(self.page_400)
        self.graphicsView_400.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_400.setBackground((96, 96, 96))
        self.graphicsView_400.setObjectName("graphicsView_400")

        self.line_400 = QtWidgets.QFrame(self.page_400)
        self.line_400.setGeometry(QtCore.QRect(610, 50, 20, 721))
        self.line_400.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_400.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_400.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_400.setObjectName("line_400")

        self.line_401 = QtWidgets.QFrame(self.page_400)
        self.line_401.setGeometry(QtCore.QRect(620, 380, 871, 11))
        self.line_401.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_401.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_401.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_401.setObjectName("line_401")

        self.scrollArea_400 = QtWidgets.QScrollArea(self.page_400)
        self.scrollArea_400.setGeometry(QtCore.QRect(40, 160, 501, 301))
        self.scrollArea_400.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea_400.setFont(font)
        self.scrollArea_400.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                          "border: 0px solid;\n"
                                          "border-radius:5px;\n"
                                          "")
        self.scrollArea_400.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_400.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_400.setWidgetResizable(True)
        self.scrollArea_400.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_400 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_400.setGeometry(QtCore.QRect(0, 0, 400, 301))
        self.scrollAreaWidgetContents_400.setObjectName("scrollAreaWidgetContents_400")
        self.gridLayout_400 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_400)
        self.gridLayout_400.setObjectName("gridLayout_400")
        self.textBrowser_400 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_400.sizePolicy().hasHeightForWidth())
        self.textBrowser_400.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser_400.setFont(font)
        self.textBrowser_400.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_400.setStyleSheet("background-color: rgb(160, 160, 160);\n"
                                           "border-radius:5px;\n"
                                           "")
        self.textBrowser_400.setObjectName("textBrowser_400")
        self.gridLayout_400.addWidget(self.textBrowser_400, 0, 0, 1, 1)
        self.scrollArea_400.setWidget(self.scrollAreaWidgetContents_400)

        self.label_402 = QtWidgets.QLabel(self.page_400)
        self.label_402.setGeometry(QtCore.QRect(40, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_402.setFont(font)
        self.label_402.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_402.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_402.setObjectName("label_402")

        self.lineEdit_400 = QtWidgets.QLineEdit(self.page_400)
        self.lineEdit_400.setGeometry(QtCore.QRect(970, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_400.setFont(font)
        self.lineEdit_400.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_400.setObjectName("lineEdit_400")

        self.lineEdit_401 = QtWidgets.QLineEdit(self.page_400)
        self.lineEdit_401.setGeometry(QtCore.QRect(250, 510, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_401.setFont(font)
        self.lineEdit_401.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_401.setObjectName("lineEdit_401")

        self.tableWidget_400 = QtWidgets.QTableWidget(self.page_400)
        self.tableWidget_400.setGeometry(QtCore.QRect(670, 210, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_400.setFont(font)
        self.tableWidget_400.setStyleSheet("QTableWidget { \n"
                                           "    selection-background-color: rgb(100, 100,100);\n"
                                           "    font: 9pt \"Segoe UI\";\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    background-color: rgb(192, 192, 192);\n"
                                           "    padding: 10px;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "QScrollBar:horizontal {\n"
                                           "    border: none;\n"
                                           "    background: rgb(52, 59, 72);\n"
                                           "    height: 10px;\n"
                                           "    margin: 0px 21px 0 21px;\n"
                                           "    border-radius: 0px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "QHeaderView::section:horizontal\n"
                                           "{\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 1px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    PointSize:10;\n"
                                           "    \n"
                                           "}\n"
                                           "QHeaderView::section:vertical\n"
                                           "{\n"
                                           "    border: 1px solid rgb(32, 34, 42);\n"
                                           "    background-color: rgb(96, 96, 96);\n"
                                           "    padding: 3px;\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "    border-top-left-radius: 0px;\n"
                                           "    border-top-right-radius: 0px;\n"
                                           "}")
        self.tableWidget_400.setRowCount(2)
        self.tableWidget_400.setObjectName("tableWidget_400")
        self.tableWidget_400.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_400.setHorizontalHeaderItem(3, item)

        self.pushButton_406 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_406.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_406.setFont(font)
        self.pushButton_406.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_406.setIcon(icon16)
        self.pushButton_406.setObjectName("pushButton_406")

        self.pushButton_407 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_407.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_407.setFont(font)
        self.pushButton_407.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_407.setIcon(icon16)
        self.pushButton_407.setObjectName("pushButton_407")

        self.pushButton_408 = QtWidgets.QPushButton(self.page_400)
        self.pushButton_408.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_408.setFont(font)
        self.pushButton_408.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(96, 96, 96);\n"
                                          "  color: rgb(0,0,0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 0px;\n"
                                          "}\n"
                                          "QPushButton:hover{ \n"
                                          "background-color: rgb(85, 170, 255);\n"
                                          "}")
        self.pushButton_408.setIcon(icon17)
        self.pushButton_408.setObjectName("pushButton_408")

        self.label_403 = QtWidgets.QLabel(self.page_400)
        self.label_403.setGeometry(QtCore.QRect(40, 520, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_403.setFont(font)
        self.label_403.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_403.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_403.setObjectName("label_403")

        self.label_404 = QtWidgets.QLabel(self.page_400)
        self.label_404.setGeometry(QtCore.QRect(690, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_404.setFont(font)
        self.label_404.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_404.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_404.setObjectName("label_404")

        self.label_405 = QtWidgets.QLabel(self.page_400)
        self.label_405.setGeometry(QtCore.QRect(1110, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_405.setFont(font)
        self.label_405.setStyleSheet("\n"
                                     "background-color: rgb(224, 224, 224);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "")
        self.label_405.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_405.setObjectName("label_405")

        self.lineEdit_402 = QtWidgets.QLineEdit(self.page_400)
        self.lineEdit_402.setGeometry(QtCore.QRect(1350, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_402.setFont(font)
        self.lineEdit_402.setStyleSheet("background-color: rgb(245, 245, 245);\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 5px;")
        self.lineEdit_402.setObjectName("lineEdit_402")

        self.frame_400.raise_()
        self.pushButton_403.raise_()
        self.groupBox_400.raise_()
        self.label_400.raise_()
        self.label_401.raise_()
        self.pushButton_404.raise_()
        self.graphicsView_400.raise_()
        self.line_400.raise_()
        self.scrollArea_400.raise_()
        self.label_402.raise_()
        self.lineEdit_400.raise_()
        self.lineEdit_401.raise_()
        self.tableWidget_400.raise_()
        self.pushButton_405.raise_()
        self.pushButton_406.raise_()
        self.pushButton_407.raise_()
        self.pushButton_408.raise_()
        self.label_403.raise_()
        self.label_404.raise_()
        self.stackedWidget.addWidget(self.page_400)





        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")

        self.frame_5 = QtWidgets.QFrame(self.page_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.frame_5.setStyleSheet("background-color: rgb(21, 21, 21);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(0, 50, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(600, 50, 891, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(192, 192, 192);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")

        self.line_6 = QtWidgets.QFrame(self.page_4)
        self.line_6.setGeometry(QtCore.QRect(580, 50, 20, 721))
        self.line_6.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.pushButton_43 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_43.setGeometry(QtCore.QRect(0, 22, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(192, 192, 192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_43.setObjectName("pushButton_43")

        self.pushButton_44 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_44.setGeometry(QtCore.QRect(139, 22, 140, 31))
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("QPushButton{\n"
                                         " background-color: rgb(160, 160, 160);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border-bottom-color: rgb(50, 57, 66);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 2px;}\n"
                                         "QPushButton:hover{ \n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_44.setObjectName("pushButton_44")

        self.pushButton_19 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 240, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("\n"
"QPushButton{\n"
"  background-color: rgb(192, 192, 192);\n"
"\n"
" color: rgb(0,0,0);\n"
" border:1px solid;\n"
"\n"
"border-radius: 5px;}\n"
"QPushButton:hover{ \n"
"\n"
"    \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_19.setIcon(icon14)
        self.pushButton_19.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_19.setObjectName("pushButton_19")

        self.groupBox_2 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_2.setGeometry(QtCore.QRect(970, 130, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"color: rgb(255,255,255);\n"
" border:0px solid;\n"
"\n"
"border-radius: 7px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("background-color: rgb(160,160,160);\n"
"color: rgb(16, 16, 16);\n"
"\n")
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("background-color: rgb(160,160,160);\n"
"color: rgb(13, 13, 13);\n")
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("background-color: rgb(160,160,160);\n"
"color: rgb(16, 16, 16);\n"
"\n")
        self.radioButton_5.setCheckable(True)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_8 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_8.setGeometry(QtCore.QRect(1080, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "border-radius: 7px;\n"
                                         "\n")
        self.radioButton_8.setCheckable(True)
        self.radioButton_8.setChecked(False)
        self.radioButton_8.setObjectName("radioButton_8")

        self.groupBox_4 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_4.setGeometry(QtCore.QRect(1220, 130, 91, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                      "color: rgb(255,255,255);\n"
                                      " border:0px solid;\n"
                                      "\n"
                                      "border-radius: 7px;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupbox_4")

        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "\n")
        self.radioButton_9.setCheckable(True)
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setObjectName("radioButton_9")

        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setStyleSheet("background-color:rgb(160,160,160);\n"
                                         "color: rgb(13, 13, 13);\n")
        self.radioButton_10.setObjectName("radioButton_10")

        self.label_58 = QtWidgets.QLabel(self.page_4)
        self.label_58.setGeometry(QtCore.QRect(1040, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "")
        self.label_58.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")

        self.label_59 = QtWidgets.QLabel(self.page_4)
        self.label_59.setGeometry(QtCore.QRect(1250, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n")
        self.label_59.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")

        self.combobox = QtWidgets.QComboBox(self.page_4)
        self.combobox.setGeometry(QtCore.QRect(1150, 140, 61, 21))
        self.combobox.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'])

        self.label_alpha = QtWidgets.QLabel(self.page_4)
        self.label_alpha.setGeometry(QtCore.QRect(1160, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_alpha.setFont(font)
        self.label_alpha.setStyleSheet("\n"
                                    "background-color: rgb(224, 224, 224);\n"
                                    "color: rgb(0, 0, 0);\n")
        self.label_alpha.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_alpha.setObjectName("label_alpha")

        self.combobox2 = QtWidgets.QComboBox(self.page_4)
        self.combobox2.setGeometry(QtCore.QRect(455, 140, 61, 21))
        self.combobox2.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'])

        self.label_alpha2 = QtWidgets.QLabel(self.page_4)
        self.label_alpha2.setGeometry(QtCore.QRect(465, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_alpha2.setFont(font)
        self.label_alpha2.setStyleSheet("\n"
                                       "background-color: rgb(224, 224, 224);\n"
                                       "color: rgb(0, 0, 0);\n")
        self.label_alpha2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_alpha2.setObjectName("label_alpha2")

        self.line_14 = QtWidgets.QFrame(self.page_4)
        self.line_14.setGeometry(QtCore.QRect(600, 390, 871, 11))
        self.line_14.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_14.setObjectName("line_14")

        self.groupBox_5 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_5.setGeometry(QtCore.QRect(260, 200, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                      "color: rgb(255,255,255);\n"
                                      " border:0px solid;\n"
                                      "\n"
                                      "border-radius: 7px;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")

        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "\n")
        self.radioButton_11.setCheckable(True)
        self.radioButton_11.setChecked(False)
        self.radioButton_11.setObjectName("radioButton_11")

        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(13, 13, 13);\n")
        self.radioButton_12.setObjectName("radioButton_12")

        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_13.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "\n")
        self.radioButton_13.setCheckable(True)
        self.radioButton_13.setChecked(False)
        self.radioButton_13.setObjectName("radioButton_13")

        self.radioButton_14 = QtWidgets.QRadioButton(self.page_4)
        self.radioButton_14.setGeometry(QtCore.QRect(370, 270, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                          "border-radius: 7px;\n"
                                         "\n")
        self.radioButton_14.setCheckable(True)
        self.radioButton_14.setChecked(False)
        self.radioButton_14.setObjectName("radioButton_14")

        self.groupBox_6 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_6.setGeometry(QtCore.QRect(455, 200, 91, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("background-color: rgb(192, 192, 192);\n"
                                      "color: rgb(255,255,255);\n"
                                      " border:0px solid;\n"
                                      "\n"
                                      "border-radius: 7px;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")

        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_15.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(30)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setStyleSheet("background-color: rgb(160,160,160);\n"
                                         "color: rgb(16, 16, 16);\n"
                                         "\n")
        self.radioButton_15.setCheckable(True)
        self.radioButton_15.setChecked(False)
        self.radioButton_15.setObjectName("radioButton_15")

        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_16.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setStyleSheet("background-color: rgb(160,160,160);\n"
                                          "color: rgb(13, 13, 13);\n")
        self.radioButton_16.setObjectName("radioButton_16")

        self.pushButton_20 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_20.setGeometry(QtCore.QRect(700, 195, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "  background-color: rgb(192,192,192);\n"
                                         "\n"
                                         " color: rgb(0,0,0);\n"
                                         " border:1px solid;\n"
                                         "\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover{ \n"
                                         "\n"
                                         "background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.pushButton_20.setIcon(icon15)
        self.pushButton_20.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_20.setObjectName("pushButton_20")

        self.graphicsView_3 = PlotWidget(self.page_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(670, 420, 701, 321))
        self.graphicsView_3.setBackground((96, 96, 96))
        self.graphicsView_3.setObjectName("graphicsView_3")

        self.pushButton_21 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_21.setGeometry(QtCore.QRect(680, 240, 101, 43))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"    background-color: rgb(192, 192, 192);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(255, 193, 69);\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon16)
        self.pushButton_21.setObjectName("pushButton_21")

        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_3.setGeometry(QtCore.QRect(80, 400, 501, 331))
        self.scrollArea_3.setMinimumSize(QtCore.QSize(50, 40))
        self.scrollArea_3.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"border: 0px solid;\n"
"border-radius:5px;\n"
"")
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 480, 331))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_13.sizePolicy().hasHeightForWidth())
        self.textBrowser_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser_13.setFont(font)
        self.textBrowser_13.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_13.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"border-radius:5px;\n"
"")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout_3.addWidget(self.textBrowser_13, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.lineEdit = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit.setGeometry(QtCore.QRect(760, 140, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: 1px solid;\n"
"border-radius: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(670, 230, 721, 151))
        self.tableWidget_3.setStyleSheet("QTableWidget { \n"
"    selection-background-color: rgb(100, 100,100);\n"
"    font: 9pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(192, 192, 192);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 10px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 1px;\n"
"    color: rgb(0, 0, 0);\n"
"    PointSize:10;\n"
"    \n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(96, 96, 96);\n"
"    padding: 3px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}")
        self.tableWidget_3.setRowCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)

        self.pushButton_27 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_27.setGeometry(QtCore.QRect(1371, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_27.setIcon(icon16)
        self.pushButton_27.setObjectName("pushButton_27")

        self.pushButton_28 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_28.setGeometry(QtCore.QRect(1371, 500, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_28.setIcon(icon16)
        self.pushButton_28.setObjectName("pushButton_28")

        self.pushButton_29 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_29.setGeometry(QtCore.QRect(1371, 690, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton{\n"
"    background-color: rgb(96, 96, 96);\n"
"  color: rgb(0,0,0);\n"
"border: 0px solid;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_29.setIcon(icon17)
        self.pushButton_29.setObjectName("pushButton_29")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.label_53 = QtWidgets.QLabel(self.page_4)
        self.label_53.setGeometry(QtCore.QRect(80, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")

        self.label_54 = QtWidgets.QLabel(self.page_4)
        self.label_54.setGeometry(QtCore.QRect(80, 360, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")

        self.label_55 = QtWidgets.QLabel(self.page_4)
        self.label_55.setGeometry(QtCore.QRect(710, 100, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("\n"
"background-color: rgb(224, 224, 224);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")

        self.tableWidget_3.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.line_6.raise_()
        self.pushButton_19.raise_()
        self.groupBox_2.raise_()
        self.pushButton_20.raise_()
        self.graphicsView_3.raise_()
        self.frame_5.raise_()
        self.scrollArea_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_29.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.tableWidget_3.raise_()
        self.pushButton_21.raise_()
        self.label_58.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.label_61.raise_()
        self.label_62.raise_()
        self.label_63.raise_()
        self.radioButton_8.raise_()
        self.combobox.raise_()
        self.label_alpha.raise_()
        self.stackedWidget.addWidget(self.page_4)


        self.frame.raise_()
        self.label.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.stackedWidget.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Système de recommandation hybride pour MovieLens"))
        self.label_4.setText(_translate("MainWindow", "Système de recommandation"))
        self.pushButton_7.setText(_translate("MainWindow", "Filtrage collaboratif"))
        self.pushButton_8.setText(_translate("MainWindow", "Filtrage cognitif"))
        self.pushButton_9.setText(_translate("MainWindow", "Filtrage hybride"))
        self.pushButton_10.setText(_translate("MainWindow", "Visualiser \n les données"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", ""))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Test et évaluation"))
        self.label_100.setText(_translate("MainWindow", "Test et évaluation"))
        self.pushButton_38.setText(_translate("MainWindow", "KNN"))
        self.pushButton_39.setText(_translate("MainWindow", "SVD"))
        self.pushButton_100.setText(_translate("MainWindow", "KNN"))
        self.pushButton_101.setText(_translate("MainWindow", "SVD"))
        self.label_8.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_101.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.pushButton_11.setText(_translate("MainWindow", "Recommander"))
        self.pushButton_102.setText(_translate("MainWindow", "Recommander"))
        self.pushButton_12.setText(_translate("MainWindow", "Commencer le test"))
        self.pushButton_103.setText(_translate("MainWindow", "Commencer le test"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))
        self.label_27.setText(_translate("MainWindow", "Films recommandés"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", ""))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", ""))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", ""))
        self.pushButton_30.setText(_translate("MainWindow", "Précision"))
        self.pushButton_31.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_35.setText(_translate("MainWindow", "Effacer"))
        self.pushButton_105.setText(_translate("MainWindow", "Précision"))
        self.pushButton_106.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_107.setText(_translate("MainWindow", "Effacer"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", ""))
        self.label_46.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_47.setText(_translate("MainWindow", "Nombre de voisins :"))
        self.label_103.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_50.setText(_translate("MainWindow", "Nombre d'utilisateurs"))
        self.label_51.setText(_translate("MainWindow", "Nombre de K"))
        self.label_105.setText(_translate("MainWindow", "Nombre d'utilisateurs"))
        self.pushButton_40.setText(_translate("MainWindow", "Modèle Vectoriel"))
        self.pushButton_41.setText(_translate("MainWindow", "Modèle de langue"))
        self.pushButton_42.setText(_translate("MainWindow", "Modèle Word2Vec"))
        self.pushButton_200.setText(_translate("MainWindow", "Modèle Vectoriel"))
        self.pushButton_201.setText(_translate("MainWindow", "Modèle de langue"))
        self.pushButton_202.setText(_translate("MainWindow", "Modèle Word2Vec"))
        self.pushButton_300.setText(_translate("MainWindow", "Modèle Vectoriel"))
        self.pushButton_301.setText(_translate("MainWindow", "Modèle de langue"))
        self.pushButton_302.setText(_translate("MainWindow", "Modèle Word2Vec"))
        self.pushButton_400.setText(_translate("MainWindow", "Approche I"))
        self.pushButton_401.setText(_translate("MainWindow", "Approche II"))
        self.pushButton_14.setText(_translate("MainWindow", "Recommander"))
        self.pushButton_203.setText(_translate("MainWindow", "Recommander"))
        self.pushButton_303.setText(_translate("MainWindow", "Recommander"))
        self.pushButton_403.setText(_translate("MainWindow", "Recommander"))
        self.radioButton.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_200.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_202.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_300.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_302.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_2.setText(_translate("MainWindow", "Sans LOD"))
        self.radioButton_201.setText(_translate("MainWindow", "Sans LOD"))
        self.radioButton_203.setText(_translate("MainWindow", "Sans LOD"))
        self.radioButton_301.setText(_translate("MainWindow", "Sans LOD"))
        self.radioButton_303.setText(_translate("MainWindow", "Sans LOD"))
        self.radioButton_400.setText(_translate("MainWindow", "Test rapid"))
        self.radioButton_6.setText(_translate("MainWindow", "Avec LOD"))
        self.radioButton_7.setText(_translate("MainWindow", "Sans LOD"))
        self.label_10.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_200.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_300.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_400.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_11.setText(_translate("MainWindow", "Test et évaluation"))
        self.label_201.setText(_translate("MainWindow", "Test et évaluation"))
        self.label_301.setText(_translate("MainWindow", "Test et évaluation"))
        self.label_401.setText(_translate("MainWindow", "Test et évaluation"))
        self.pushButton_16.setText(_translate("MainWindow", "Commencer le test"))
        self.pushButton_204.setText(_translate("MainWindow", "Commencer le test"))
        self.pushButton_304.setText(_translate("MainWindow", "Commencer le test"))
        self.pushButton_404.setText(_translate("MainWindow", "Commencer le test"))
        self.label_28.setText(_translate("MainWindow", "Films recommandés:"))
        self.label_202.setText(_translate("MainWindow", "Films recommandés:"))
        self.label_302.setText(_translate("MainWindow", "Films recommandés:"))
        self.label_402.setText(_translate("MainWindow", "Films recommandés:"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", ""))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", ""))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))

        item = self.tableWidget_200.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_200.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_200.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_200.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_200.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_200.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))

        item = self.tableWidget_300.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_300.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_300.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_300.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_300.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_300.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))

        item = self.tableWidget_400.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_400.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_400.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_400.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_400.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_400.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))

        self.pushButton_32.setText(_translate("MainWindow", "Précision"))
        self.pushButton_206.setText(_translate("MainWindow", "Précision"))
        self.pushButton_306.setText(_translate("MainWindow", "Précision"))
        self.pushButton_406.setText(_translate("MainWindow", "Précision"))
        self.pushButton_33.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_207.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_307.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_407.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_34.setText(_translate("MainWindow", "Effacer"))
        self.pushButton_208.setText(_translate("MainWindow", "Effacer"))
        self.pushButton_308.setText(_translate("MainWindow", "Effacer"))
        self.pushButton_408.setText(_translate("MainWindow", "Effacer"))
        self.label_48.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_49.setText(_translate("MainWindow", "Nombre d\'utilisateurs "))
        self.label_203.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_204.setText(_translate("MainWindow", "Nombre d\'utilisateurs "))
        self.label_303.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_304.setText(_translate("MainWindow", "Nombre d\'utilisateurs "))
        self.label_403.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_404.setText(_translate("MainWindow", "Nombre de couches MLP"))
        self.label_405.setText(_translate("MainWindow", "Nombre de neurones"))
        self.label_13.setText(_translate("MainWindow", "Résultats de recommandation"))
        self.label_14.setText(_translate("MainWindow", "Test et évaluation"))
        self.pushButton_43.setText(_translate("MainWindow", "Approche I"))
        self.pushButton_44.setText(_translate("MainWindow", "Approche II"))
        self.pushButton_19.setText(_translate("MainWindow", "Recommnder"))
        self.radioButton_3.setText(_translate("MainWindow", "TF/IDF"))
        self.radioButton_4.setText(_translate("MainWindow", "ML"))
        self.radioButton_5.setText(_translate("MainWindow", "W2V"))
        self.radioButton_8.setText(_translate("MainWindow", "LOD"))
        self.radioButton_9.setText(_translate("MainWindow", "KNN"))
        self.radioButton_10.setText(_translate("MainWindow", "SVD"))
        self.radioButton_11.setText(_translate("MainWindow", "TF/IDF"))
        self.radioButton_12.setText(_translate("MainWindow", "ML"))
        self.radioButton_13.setText(_translate("MainWindow", "W2V"))
        self.radioButton_14.setText(_translate("MainWindow", "LOD"))
        self.radioButton_15.setText(_translate("MainWindow", "KNN"))
        self.radioButton_16.setText(_translate("MainWindow", "SVD"))
        self.label_58.setText(_translate("MainWindow", "FBC"))
        self.label_59.setText(_translate("MainWindow", "FC"))
        self.label_alpha.setText(_translate("MainWindow", "alpha"))
        self.label_alpha2.setText(_translate("MainWindow", "alpha"))
        self.label_60.setText(_translate("MainWindow", "DataSet de test"))
        self.label_61.setText(_translate("MainWindow", "DataSet d'apprentissage"))
        self.label_62.setText(_translate("MainWindow", "DataSet de test"))
        self.label_63.setText(_translate("MainWindow", "DataSet d'apprentissage"))
        self.pushButton_45.setText(_translate("MainWindow", "..."))
        self.pushButton_46.setText(_translate("MainWindow", "..."))
        self.pushButton_20.setText(_translate("MainWindow", "Commencer le test"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", ""))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", ""))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))
        self.pushButton_27.setText(_translate("MainWindow", "Précision"))
        self.pushButton_28.setText(_translate("MainWindow", "NDCG"))
        self.pushButton_29.setText(_translate("MainWindow", "Effacer"))
        self.label_53.setText(_translate("MainWindow", "ID de l\'utilisateur :"))
        self.label_54.setText(_translate("MainWindow", "Films recommandés :"))
        self.label_55.setText(_translate("MainWindow", "Nombre d\'utilisateurs"))
        item = self.tableWidget_100.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Précision"))
        item = self.tableWidget_100.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "NDCG"))
        item = self.tableWidget_100.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "@10"))
        item = self.tableWidget_100.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "@15"))
        item = self.tableWidget_100.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "@20"))
        item = self.tableWidget_100.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "@30"))

        # les actiooons : liens vers les pages

        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_7.clicked.connect(lambda: self.pushButton_7.setStyleSheet("QPushButton{\n"
                                            " background-color: rgb(21, 21, 21);\n"
                                            "\n"
                                            " color: rgb(255,255,255);\n"
                                            " border:1px solid;\n"
                                            "\n"
                                            "border-radius: 5px;}\n"
                                            "QPushButton:hover{ \n"
                                            "background-color: rgb(85, 170, 255);\n"
                                            "}"))
        self.pushButton_7.clicked.connect(lambda: self.pushButton_8.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_7.clicked.connect(lambda: self.pushButton_9.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_7.clicked.connect(lambda: self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))

        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_8.clicked.connect(lambda: self.pushButton_8.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(21, 21, 21);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_8.clicked.connect(lambda: self.pushButton_7.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_8.clicked.connect(lambda: self.pushButton_9.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_8.clicked.connect(lambda: self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))

        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.pushButton_9.clicked.connect(lambda: self.pushButton_9.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(21, 21, 21);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_9.clicked.connect(lambda: self.pushButton_7.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_9.clicked.connect(lambda: self.pushButton_8.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_9.clicked.connect(lambda: self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))

        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_4.clicked.connect(lambda: self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(21, 21, 21);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_4.clicked.connect(lambda: self.pushButton_7.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_4.clicked.connect(lambda: self.pushButton_8.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))
        self.pushButton_4.clicked.connect(lambda: self.pushButton_9.setStyleSheet("QPushButton{\n"
                                                                                  " background-color: rgb(40, 45, 50);\n"
                                                                                  "\n"
                                                                                  " color: rgb(255,255,255);\n"
                                                                                  " border:1px solid;\n"
                                                                                  "\n"
                                                                                  "border-radius: 5px;}\n"
                                                                                  "QPushButton:hover{ \n"
                                                                                  "background-color: rgb(85, 170, 255);\n"
                                                                                  "}"))

        self.pushButton_200.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_300.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_41.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_200))
        self.pushButton_301.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_200))
        self.pushButton_42.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_300))
        self.pushButton_202.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_300))
        self.pushButton_400.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.pushButton_44.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_400))
        self.pushButton_39.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_10))
        self.pushButton_100.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        # quitter l'application
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        # les fonctions de lapproche

        # precision et ndcg

        # les fonctionnalitees************************************************************************
        # afficher les resultats
        self.pushButton_10.clicked.connect(lambda: self.visualise())
        self.pushButton_14.clicked.connect(lambda: self.aff_vect())
        self.pushButton_203.clicked.connect(lambda: self.aff_ml())
        self.pushButton_303.clicked.connect(lambda: self.aff_w2v())
        self.pushButton_403.clicked.connect(lambda: self.aff_approche2())
        self.pushButton_11.clicked.connect(lambda: self.aff_knn())
        self.pushButton_102.clicked.connect(lambda: self.aff_svd())
        self.pushButton_19.clicked.connect(lambda: self.aff_hyb())

        # remplir table

        self.pushButton_12.clicked.connect(lambda: self.aff_test_KNN())
        self.pushButton_103.clicked.connect(lambda: self.aff_test_SVD())
        self.pushButton_16.clicked.connect(lambda: self.aff_test_vect())
        self.pushButton_204.clicked.connect(lambda: self.aff_test_ml())
        self.pushButton_304.clicked.connect(lambda: self.aff_test_w2v())
        self.pushButton_404.clicked.connect(lambda: self.aff_test_approche2())
        self.pushButton_20.clicked.connect(lambda: self.aff_test_hyb())
        # test KNN
        self.pushButton_31.clicked.connect(lambda: self.draw_NDCGKNN())
        self.pushButton_30.clicked.connect(lambda: self.draw_precisionKNN())
        self.pushButton_35.clicked.connect(self.graphicsView.clear)

        self.pushButton_106.clicked.connect(lambda: self.draw_NDCGSVD())
        self.pushButton_105.clicked.connect(lambda: self.draw_precisionSVD())
        self.pushButton_107.clicked.connect(self.graphicsView_100.clear)

        # test FBC
        self.pushButton_33.clicked.connect(lambda: self.draw_NDCGVect())
        self.pushButton_32.clicked.connect(lambda: self.draw_precisionVect())
        self.pushButton_34.clicked.connect(self.graphicsView_2.clear)

        self.pushButton_207.clicked.connect(lambda: self.draw_NDCGML())
        self.pushButton_206.clicked.connect(lambda: self.draw_precisionML())
        self.pushButton_208.clicked.connect(self.graphicsView_200.clear)

        self.pushButton_307.clicked.connect(lambda: self.draw_NDCGW2V())
        self.pushButton_306.clicked.connect(lambda: self.draw_precisionW2V())
        self.pushButton_308.clicked.connect(self.graphicsView_300.clear)

        self.pushButton_407.clicked.connect(lambda: self.draw_NDCGhyb2())
        self.pushButton_406.clicked.connect(lambda: self.draw_precisionhyb2())
        self.pushButton_408.clicked.connect(self.graphicsView_400.clear)

        # test hyb
        self.pushButton_27.clicked.connect(lambda: self.draw_precisionhyb())
        self.pushButton_28.clicked.connect(lambda: self.draw_NDCGhyb())
        self.pushButton_29.clicked.connect(self.graphicsView_3.clear)

        self.pushButton_45.clicked.connect(lambda: self.getPath2())
        self.pushButton_46.clicked.connect(lambda: self.getPath1())

    def draw_precisionKNN(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView.plot(x, y, pen=pen, symbol="+", symbolSize=15, symbolBrush=("g"))

            self.graphicsView.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K</span>")
            self.graphicsView.showGrid(x=True, y=True)

    def draw_NDCGKNN(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191,0))

            self.graphicsView.setLabel('left', "<span style=\"color:black;font-size:20px\">NDCG</span>")
            self.graphicsView.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView.showGrid(x=True, y=True)


    def draw_precisionSVD(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_100.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)
            y = L1
            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_100.plot(x, y, pen=pen, symbol="+", symbolSize=15, symbolBrush=("g"))

            self.graphicsView_100.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_100.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K</span>")
            self.graphicsView_100.showGrid(x=True, y=True)

    def draw_NDCGSVD(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_100.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)
            y = L1
            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_100.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191,0))

            self.graphicsView_100.setLabel('left', "<span style=\"color:black;font-size:20px\">NDCG</span>")
            self.graphicsView_100.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_100.showGrid(x=True, y=True)


    def draw_precisionVect(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget_2.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_2.plot(x, y, pen=pen, symbol="+", symbolSize=10, symbolBrush=("g"))

            self.graphicsView_2.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_2.setLabel('bottom', "<span style=\"color:black;font-size:20px\"> @K </span>")
            self.graphicsView_2.showGrid(x=True, y=True)

    def draw_NDCGVect(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_2.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)
            y = L1
            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_2.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191,0))

            self.graphicsView_2.setLabel('left', "<span style=\"color:black;font-size:20px\">NDCG</span>")
            self.graphicsView_2.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_2.showGrid(x=True, y=True)

    def draw_precisionML(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_200.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1
            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_200.plot(x, y, pen=pen, symbol="+", symbolSize=10, symbolBrush=("g"))

            self.graphicsView_200.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_200.setLabel('bottom', "<span style=\"color:black;font-size:20px\"> @K </span>")
            self.graphicsView_200.showGrid(x=True, y=True)


    def draw_NDCGML(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_200.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)
            y = L1
            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_200.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191, 0))

            self.graphicsView_200.setLabel('left', "<span style=\"color:black;font-size:20px\">NDCG</span>")
            self.graphicsView_200.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_200.showGrid(x=True, y=True)

    def draw_precisionW2V(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_300.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1
            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_300.plot(x, y, pen=pen, symbol="+", symbolSize=10, symbolBrush=("g"))

            self.graphicsView_300.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_300.setLabel('bottom', "<span style=\"color:black;font-size:20px\"> @K </span>")
            self.graphicsView_300.showGrid(x=True, y=True)

    def draw_NDCGW2V(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_300.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)
            y = L1
            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_300.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191, 0))

            self.graphicsView_300.setLabel('left', "<span style=\"color:black;font-size:20px\">NDCG</span>")
            self.graphicsView_300.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_300.showGrid(x=True, y=True)

    def draw_precisionhyb(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget_3.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_3.plot(x, y, pen=pen, symbol="t", symbolSize=15, symbolBrush=("g"))

            self.graphicsView_3.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_3.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_3.showGrid(x=True, y=True)

    def draw_NDCGhyb(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget_3.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_3.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191,0))

            self.graphicsView_3.setLabel('left', "<span style=\"color:black;font-size:18px\">NDCG</span>")
            self.graphicsView_3.setLabel('bottom', "<span style=\"color:black;font-size:18px\">@K </span>")
            self.graphicsView_3.showGrid(x=True, y=True)

    def draw_precisionhyb2(self):
            x = [10, 15, 20, 30]
            L1 = []
            for i in range(4):
                    item = self.tableWidget_400.item(0, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(244, 102, 27), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_400.plot(x, y, pen=pen, symbol="t", symbolSize=15, symbolBrush=("g"))

            self.graphicsView_400.setLabel('left', "<span style=\"color:black;font-size:20px\">Précision</span>")
            self.graphicsView_400.setLabel('bottom', "<span style=\"color:black;font-size:20px\">@K </span>")
            self.graphicsView_400.showGrid(x=True, y=True)

    def draw_NDCGhyb2(self):
            x = [10, 15, 20, 30]

            L1 = []
            for i in range(4):
                    item = self.tableWidget_400.item(1, i)
                    T = item.text()
                    L = float(T)
                    L1.append(L)

            y = L1

            pen = pg.mkPen(color=(0, 153, 0), width=3, style=QtCore.Qt.SolidLine)
            self.graphicsView_400.plot(x, y, pen=pen, symbol="o", symbolSize=15, symbolBrush=(255, 191, 0))

            self.graphicsView_400.setLabel('left', "<span style=\"color:black;font-size:18px\">NDCG</span>")
            self.graphicsView_400.setLabel('bottom', "<span style=\"color:black;font-size:18px\">@K </span>")
            self.graphicsView_400.showGrid(x=True, y=True)



    def getPath1(self):
        self.lineEdit_9.setText(QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile')[0])

    def getPath2(self):
        self.lineEdit_10.setText(QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile')[0])

    def visualise(self):
            test = pd.read_csv(self.lineEdit_9.text())
            train = pd.read_csv(self.lineEdit_10.text())
            data = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
            for line in test['rating'].values:
                    line = str(line)
                    data[line] = data[line] + 1
            data2 = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
            for line in train['rating'].values:
                    line = str(line)
                    data2[line] = data2[line] + 1

            x = list(data.keys())
            y = list(data.values())
            fig = plt.figure(figsize=(10, 5))
            plt.xlabel('Ratings')
            plt.ylabel('Count')
            plt.bar(x, y, color='maroon', width=0.4)
            plt.title("Les évaluation des utilisateurs dans le dataset d'apprentissage")
            plt.savefig('plt1.png')

            x = list(data2.keys())
            y = list(data2.values())
            fig = plt.figure(figsize=(10, 5))
            plt.xlabel('Ratings')
            plt.ylabel('Count')
            plt.bar(x, y, color='maroon', width=0.4)
            plt.title("Les évaluation des utilisateurs dans le dataset de test")
            plt.savefig('plt2.png')

            self.label_3.setStyleSheet("image: url(plt1.PNG);")
            self.label_2.setStyleSheet("image: url(plt2.PNG);")

    def aff_vect(self):
            lod = False
            if self.radioButton_6.isChecked():
                    lod = True
            if self.radioButton_7.isChecked():
                    lod = False
            self.textBrowser.append(affiche_list_vect(int(self.lineEdit_7.text()), 15, lod))

    def aff_test_vect(self):
            lod = False
            if self.radioButton.isChecked():
                    lod = True
            if self.radioButton_2.isChecked():
                    lod = False
            results = affiche_tests_vect(int(self.lineEdit_6.text()), lod)
            for i in range(4):
                    self.tableWidget_2.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_2.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_ml(self):
            lod = False
            if self.radioButton_202.isChecked():
                    lod = True
            if self.radioButton_203.isChecked():
                    lod = False
            self.textBrowser_200.append(affiche_list_ml(int(self.lineEdit_201.text()), 15, lod))

    def aff_test_ml(self):
            lod = False
            if self.radioButton_200.isChecked():
                    lod = True
            if self.radioButton_201.isChecked():
                    lod = False
            results = affiche_tests_ml(int(self.lineEdit_200.text()), lod)
            for i in range(4):
                    self.tableWidget_200.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_200.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))


    def aff_w2v(self):
            lod = False
            if self.radioButton_302.isChecked():
                    lod = True
            if self.radioButton_303.isChecked():
                    lod = False
            self.textBrowser_300.append(affiche_list_w2v(int(self.lineEdit_301.text()), 15, lod))

    def aff_test_w2v(self):
            lod = False
            if self.radioButton_300.isChecked():
                    lod = True
            if self.radioButton_301.isChecked():
                    lod = False
            results = affiche_tests_w2v(int(self.lineEdit_300.text()), lod)
            for i in range(4):
                    self.tableWidget_300.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_300.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_approche2(self):
            self.textBrowser_400.append(affiche_list_app2(int(self.lineEdit_401.text())))

    def aff_test_approche2(self):
            if self.radioButton_400.isChecked():
                results = affiche_tests_app2()
            else:
                results = affiche_tests_train(self.lineEdit_400.text(), self.lineEdit_402.text())
            for i in range(4):
                    self.tableWidget_400.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_400.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_knn(self):
            self.textBrowser_11.append(affiche_lists_knn(int(self.lineEdit_4.text()), int(self.lineEdit_5.text())))

    def aff_test_KNN(self):
            results = affiche_tests_knn(int(self.lineEdit_3.text()), int(self.lineEdit_13.text()))
            for i in range(4):
                    self.tableWidget.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_svd(self):
            self.textBrowser_100.append(affiche_lists_svd(int(self.lineEdit_101.text())))

    def aff_test_SVD(self):
            results = affiche_tests_svd(int(self.lineEdit_100.text()))
            for i in range(4):
                    self.tableWidget_100.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_100.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_test_hyb(self):
            if self.radioButton_8.isChecked():
                    if self.radioButton_3.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn vect-lod")
                                    results = affiche_tests_hyb_vect_lod_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd vect-lod")
                                    results = affiche_tests_hyb_vect_lod_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                    if self.radioButton_4.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn ml-lod")
                                    results = affiche_tests_hyb_ml_lod_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd ml-lod")
                                    results = affiche_tests_hyb_ml_lod_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                    if self.radioButton_5.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn w2v-lod")
                                    results = affiche_tests_hyb_w2v_LOD_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd w2v-lod")
                                    results = affiche_tests_hyb_w2v_LOD_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])

            if not self.radioButton_8.isChecked():
                    if self.radioButton_3.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn vect")
                                    results = affiche_tests_hyb_vect_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd vect")
                                    results = affiche_tests_hyb_vect_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                    if self.radioButton_4.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn ml")
                                    results = affiche_tests_hyb_ml_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd ml")
                                    results = affiche_tests_hyb_ml_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                    if self.radioButton_5.isChecked():
                            if self.radioButton_9.isChecked():
                                    print("knn w2v")
                                    results = affiche_tests_hyb_w2v_knn(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])
                            if self.radioButton_10.isChecked():
                                    print("svd w2v")
                                    results = affiche_tests_hyb_w2v_svd(int(self.lineEdit.text()),
                                                                         self.combobox.currentText()[2])

            for i in range(4):
                    self.tableWidget_3.setItem(0, i, QTableWidgetItem('{:.2f}'.format(results[i][0])))
                    self.tableWidget_3.setItem(1, i, QTableWidgetItem('{:.2f}'.format(results[i][1])))

    def aff_hyb(self):
            if self.radioButton_14.isChecked():
                    if self.radioButton_11.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn vect-lod")
                                    results = affiche_list_hyb_vect_lod_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd vect-lod")
                                    results = affiche_list_hyb_vect_lod_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                    if self.radioButton_12.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn ml-lod")
                                    results = affiche_list_hyb_ml_lod_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd ml-lod")
                                    results = affiche_list_hyb_ml_lod_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                    if self.radioButton_13.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn w2v-lod")
                                    results = affiche_list_hyb_w2v_lod_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd w2v-lod")
                                    results = affiche_list_hyb_w2v_lod_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])

            if not self.radioButton_14.isChecked():
                    if self.radioButton_11.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn vect")
                                    results = affiche_list_hyb_vect_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd vect")
                                    results = affiche_list_hyb_vect_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                    if self.radioButton_12.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn ml")
                                    results = affiche_list_hyb_ml_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd ml")
                                    results = affiche_list_hyb_ml_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                    if self.radioButton_13.isChecked():
                            if self.radioButton_15.isChecked():
                                    print("knn w2v")
                                    results = affiche_list_hyb_w2v_knn(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
                            if self.radioButton_16.isChecked():
                                    print("svd w2v")
                                    results = affiche_list_hyb_w2v_svd(int(self.lineEdit_2.text()),
                                                                         self.combobox2.currentText()[2])
            self.textBrowser_13.append(results)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
