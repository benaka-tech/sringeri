# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
import mysql
import mysql.connector as mc
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from datetime import datetime
import xlwt
import pandas.io.sql as sql

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 971)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 190, 91, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/QDkO7nK6-removebg-preview.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 461, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/logo_colour.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 130, 301, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/download__2_-removebg-preview.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 190, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/aic-jitf-logo (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 260, 801, 571))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 431, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 381, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 270, 381, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 20, 321, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 231, 161))
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setLineWidth(5)
        self.label_13.setMidLineWidth(5)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_13.setScaledContents(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 170, 281, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(460, 310, 321, 251))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(40, 20, 231, 161))
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setLineWidth(5)
        self.label_15.setMidLineWidth(5)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_15.setScaledContents(True)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 281, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 450, 91, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(224, 452, 101, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(70, 880, 761, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer1 = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer1.timeout.connect(self.viewCam1)
        # set control_bt callback clicked  function
        self.pushButton.clicked.connect(self.controlTimer)
        self.pushButton_2.clicked.connect(self.caputure)
        self.pushButton_3.clicked.connect(self.sumbit)
        self.pushButton_5.clicked.connect(self.controlTimer1)
        self.pushButton_6.clicked.connect(self.caputure1)
        self.pushButton_4.clicked.connect(self.export_report)
        val = 40
        if val > 45:
            self.label_16.setStyleSheet("background-color: red")
            self.label_12.setText(str(val))
        else:
            self.label_7.setStyleSheet("background-color: green")
            self.label_12.setText(str(val))

    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_13.setPixmap(QPixmap.fromImage(qImg))

    def viewCam1(self):
        # read image in BGR format
        ret, image = self.cap1.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_15.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.pushButton.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.pushButton.setText("Start")

    def controlTimer1(self):
        # if timer is stopped
        if not self.timer1.isActive():
            # create video capture
            self.cap1 = cv2.VideoCapture(0)
            # start timer
            self.timer1.start(20)
            # update control_bt text
            self.pushButton_5.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer1.stop()
            # release video capture
            self.cap1.release()
            # update control_bt text
            self.pushButton_5.setText("Start")

    def caputure(self):
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            self.file = '%s.jpg' % (str(datetime.now().strftime("%Y%m%d%H%M%S")))
            cv2.imwrite('C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photo-%s.png' % (
                str(datetime.now().strftime("%Y%m%d%H%M%S"))), frame)
            f = open("C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos.txt", "a")
            f.write('\n')
            f.write('file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos-%s.png' % (
                str(datetime.now().strftime("%Y%m%d%H%M%S"))))
            f.close()
            break

    def caputure1(self):
        while (self.cap1.isOpened()):
            ret, frame = self.cap1.read()
            self.file1 = '%s.jpg' % (str('id' + datetime.now().strftime("%Y%m%d%H%M%S")))
            cv2.imwrite('C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-%s.png' % (
                str(datetime.now().strftime("%Y%m%d%H%M%S"))), frame)
            f = open("C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\ids.txt", "a")
            f.write('\n')
            f.write('file:///C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\id-%s.png' % (
                str(datetime.now().strftime("%Y%m%d%H%M%S"))))
            f.close()
            break

    def sumbit(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex1 = "(0/91)?[7-9][0-9]{9}"
        name = self.lineEdit.text()
        state = self.comboBox.currentText()
        address = self.lineEdit_2.text()
        emailid = self.lineEdit_5.text()
        phoneno = self.lineEdit_6.text()
        if not (re.search(regex, emailid)):
            self.label_14.setText("Invaild Email")
        if not (re.compile("(0/91)?[7-9][0-9]{9}").match(phoneno)):
            self.label_14.setText("Invaild Phone")

        with open("C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\photos\\photos.txt", "r") as file:
            for last_line in file:
                pass
        filename = str(last_line)
        with open("C:\\Users\\Benaka\\PycharmProjects\\pythonProject\\img\\ids\\ids.txt", "r") as file:
            for last_line1 in file:
                pass
        filename2 = str(last_line1)

        print(name, address, state, address, emailid, phoneno, filename)
        if (re.search(regex, emailid) and re.compile("(0/91)?[7-9][0-9]{9}").match(phoneno)):

         conn = mysql.connector.connect(
             user='root', password='', host='localhost', database='project')

        # Creating a cursor object using the cursor() method
         cursor = conn.cursor()

        # Preparing SQL query to INSERT a record into the database.
         insert_stmt = (
            "INSERT INTO `devotees_details`(`name`, `address`, `state`, `email`, `phone`, `photo`, `id_card`) VALUES (%s, %s, %s, %s, %s, %s ,%s)"

         )
         data = (name, address, state, emailid, phoneno, filename, filename2)

         try:
            # Executing the SQL command
             cursor.execute(insert_stmt, data)

            # Commit your changes in the database
             conn.commit()

         except mysql.connector.Error as e:
             print(e)

            # Rolling back in case of error
             conn.rollback()

         print("Data inserted")

         # Closing the connection
         conn.close()
         self.lineEdit.clear()
         self.lineEdit_2.clear()
         self.lineEdit_5.clear()
         self.lineEdit_6.clear()

    def export_report(self):
        # connect the mysql with the python
        con = mc.connect(user="root", password="", host="localhost", database="project")
        # read the data
        df = sql.read_sql('SELECT * FROM devotees_details', con)
        # print the data
        print(df)
        # export the data into the excel sheet
        df.to_excel('ds.xls')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Devotees  Details"))
        self.label_5.setText(_translate("MainWindow", " Name"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        self.label_8.setText(_translate("MainWindow", "State"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Arunachal Pradesh"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Assam"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Bihar"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Chhattisgarh"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Gujarat"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Haryana"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Himachal Pradesh"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Jharkhand"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Karnataka"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Kerala"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Maharashtra"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Manipur"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Meghalaya"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Mizoram"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Nagaland"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Odisha"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Punjab"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Rajasthan"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Sikkim"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Telangana"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Tripura"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox.setItemText(26, _translate("MainWindow", "Uttarakhand"))
        self.comboBox.setItemText(27, _translate("MainWindow", "West Bengal"))
        self.label_9.setText(_translate("MainWindow", "Email ID"))
        self.label_10.setText(_translate("MainWindow", "Phone No"))
        self.label_11.setText(_translate("MainWindow", "Temperature"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Photo"))
        self.pushButton.setText(_translate("MainWindow", "SHOW"))
        self.pushButton_2.setText(_translate("MainWindow", "CAPUTURE"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Identification Proof"))
        self.pushButton_5.setText(_translate("MainWindow", "SHOW"))
        self.pushButton_6.setText(_translate("MainWindow", "CAPUTURE"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.pushButton_4.setText(_translate("MainWindow", "Export Report"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())