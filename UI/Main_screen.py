# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import numpy as np
import cv2



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 564)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 471, 141))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 190, 861, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 371, 271))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 321, 234))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 20, 351, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 301, 211))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setLineWidth(5)
        self.label_8.setMidLineWidth(5)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 371, 251))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 331, 211))
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setLineWidth(8)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(470, 30, 341, 241))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(30, 40, 301, 181))
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setLineWidth(8)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setGeometry(QtCore.QRect(5, 10, 841, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.savePhoto)
        self.filename = 'Snapshot ' + str(time.strftime("%Y-%b-%d at %H.%M.%S %p")) + '.png'
        self.started = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/newPrefix/logo_colour.png\"/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "User Details"))
        self.label_2.setText(_translate("MainWindow", "First Name"))
        self.label_3.setText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "D.O.B"))
        self.label_5.setText(_translate("MainWindow", "Address"))
        self.label_6.setText(_translate("MainWindow", "Email ID"))
        self.label_7.setText(_translate("MainWindow", "Phone No"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Photo"))
        self.pushButton.setText(_translate("MainWindow", "SHOW"))
        self.pushButton_2.setText(_translate("MainWindow", "CAPUTURE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Identification Proof"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Temperature"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))

    def loadImage(self):
        """ This function will load the camera device, obtain the image
            and set it to label using the setPhoto function
        """
        if self.started:
            self.started = False
            self.pushButton_2.setText('Start')
        else:
            self.started = True
            self.pushButton_2.setText('Stop')

        cam = True  # True for webcam
        if cam:
            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture('video.mp4')

        cnt = 0
        frames_to_count = 20
        st = 0


        while (vid.isOpened()):

            img, self.image = vid.read()
            self.image = imutils.resize(self.image, height=480)

            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.15,
                minNeighbors=7,
                minSize=(80, 80),
                flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (10, 228, 220), 5)

            if cnt == frames_to_count:
                try:  # To avoid divide by 0 we put it in try except
                    print(frames_to_count / (time.time() - st), 'FPS')
                    self.fps = round(frames_to_count / (time.time() - st))

                    st = time.time()
                    cnt = 0
                except:
                    pass

            cnt += 1

            self.update()
            key = cv2.waitKey(1) & 0xFF
            if self.started == False:
                break
                print('Loop break')

    def savePhoto(self):
        """ This function will save the image"""
        self.filename = 'Snapshot ' + str(time.strftime("%Y-%b-%d at %H.%M.%S %p")) + '.png'
        cv2.imwrite(self.filename, self.tmp)
        print('Image saved as:', self.filename)


import img

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
