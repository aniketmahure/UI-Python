from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(-180, 0, 1250, 900))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("Use/pngguru.com-id-bvcnj.png"))
        self.label2.setScaledContents(False)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 190, 781, 551))
        self.label3.setStyleSheet("MainWindow{\n"
"setStyleSheet(“background-color: grey;”)\n"
"}")
        self.label3.setText("")
        self.label3.setPixmap(QtGui.QPixmap("Use/CircularRing.png"))
        self.label3.setObjectName("label3")
        self.StartButton = QtWidgets.QToolButton(self.centralwidget)
        self.StartButton.setEnabled(True)
        self.StartButton.setGeometry(QtCore.QRect(393, 315, 301, 301))
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.StartButton.setMouseTracking(False)
        self.StartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.StartButton.setAutoFillBackground(False)
        self.StartButton.setStyleSheet("font: 28pt \"Segoe Print\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Use/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartButton.setIcon(icon)
        self.StartButton.setIconSize(QtCore.QSize(300, 300))
        self.StartButton.setAutoRaise(True)
        self.StartButton.setArrowType(QtCore.Qt.NoArrow)
        self.StartButton.setObjectName("StartButton")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 0, 1250, 900))
        self.label1.setStyleSheet("")
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label1.setLineWidth(1)
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("Use/BlackBG.png"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.VoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.VoiceButton.setGeometry(QtCore.QRect(1090, 280, 161, 161))
        self.VoiceButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VoiceButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.VoiceButton.setStyleSheet("QPushButton{\n"
"rgb(0, 0, 0)\n"
"}")
        self.VoiceButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Use/TrainV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VoiceButton.setIcon(icon1)
        self.VoiceButton.setIconSize(QtCore.QSize(161, 161))
        self.VoiceButton.setAutoRepeat(True)
        self.VoiceButton.setAutoExclusive(True)
        self.VoiceButton.setDefault(False)
        self.VoiceButton.setObjectName("VoiceButton")
        self.FaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.FaceButton.setGeometry(QtCore.QRect(1090, 560, 161, 121))
        self.FaceButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FaceButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Use/FaceDetect.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FaceButton.setIcon(icon2)
        self.FaceButton.setIconSize(QtCore.QSize(180, 120))
        self.FaceButton.setObjectName("FaceButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(1140, 20, 61, 61))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Use/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon3)
        self.ExitButton.setIconSize(QtCore.QSize(60, 60))
        self.ExitButton.setAutoExclusive(True)
        self.ExitButton.setAutoDefault(True)
        self.ExitButton.setObjectName("ExitButton")
        self.label1.raise_()
        self.label2.raise_()
        self.label3.raise_()
        self.StartButton.raise_()
        self.VoiceButton.raise_()
        self.FaceButton.raise_()
        self.ExitButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "Train Your Voice"))
        self.VoiceButton.setToolTip(_translate("MainWindow", "Train Your Voice"))
        self.FaceButton.setToolTip(_translate("MainWindow", "Face Detect"))
        self.ExitButton.setToolTip(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
