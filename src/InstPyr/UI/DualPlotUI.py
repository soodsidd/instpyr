# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DualPlotUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .CustomWidgets.mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ControlArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlArea.sizePolicy().hasHeightForWidth())
        self.ControlArea.setSizePolicy(sizePolicy)
        self.ControlArea.setWidgetResizable(True)
        self.ControlArea.setObjectName("ControlArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 214, 821))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ControlBay = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ControlBay.sizePolicy().hasHeightForWidth())
        self.ControlBay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ControlBay.setFont(font)
        self.ControlBay.setObjectName("ControlBay")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ControlBay)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7.addWidget(self.ControlBay)
        self.Plotting = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Plotting.sizePolicy().hasHeightForWidth())
        self.Plotting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Plotting.setFont(font)
        self.Plotting.setObjectName("Plotting")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Plotting)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.Plotting)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Sampling = QtWidgets.QDoubleSpinBox(self.Plotting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sampling.sizePolicy().hasHeightForWidth())
        self.Sampling.setSizePolicy(sizePolicy)
        self.Sampling.setMaximumSize(QtCore.QSize(53, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Sampling.setFont(font)
        self.Sampling.setDecimals(1)
        self.Sampling.setMinimum(0.1)
        self.Sampling.setSingleStep(0.1)
        self.Sampling.setProperty("value", 1.0)
        self.Sampling.setObjectName("Sampling")
        self.horizontalLayout_3.addWidget(self.Sampling)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.clear = QtWidgets.QPushButton(self.Plotting)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.verticalLayout_5.addWidget(self.clear)
        self.verticalLayout_7.addWidget(self.Plotting)
        self.Logging = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Logging.sizePolicy().hasHeightForWidth())
        self.Logging.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Logging.setFont(font)
        self.Logging.setObjectName("Logging")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Logging)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.Logging)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.filename = QtWidgets.QTextEdit(self.Logging)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)
        self.filename.setMinimumSize(QtCore.QSize(0, 50))
        self.filename.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.filename.setFont(font)
        self.filename.setObjectName("filename")
        self.verticalLayout.addWidget(self.filename)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.Logging)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.LogEnable = QtWidgets.QCheckBox(self.Logging)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LogEnable.setFont(font)
        self.LogEnable.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LogEnable.setText("")
        self.LogEnable.setObjectName("LogEnable")
        self.horizontalLayout_5.addWidget(self.LogEnable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addWidget(self.Logging)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.ControlArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.ControlArea)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Mainplot_top = MplWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.Mainplot_top.sizePolicy().hasHeightForWidth())
        self.Mainplot_top.setSizePolicy(sizePolicy)
        self.Mainplot_top.setObjectName("Mainplot_top")
        self.verticalLayout_3.addWidget(self.Mainplot_top)
        self.Mainplot_bottom = MplWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.Mainplot_bottom.sizePolicy().hasHeightForWidth())
        self.Mainplot_bottom.setSizePolicy(sizePolicy)
        self.Mainplot_bottom.setObjectName("Mainplot_bottom")
        self.verticalLayout_3.addWidget(self.Mainplot_bottom)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(MainWindow.eventHandler)
        self.Sampling.valueChanged['double'].connect(MainWindow.eventHandler)
        self.LogEnable.clicked.connect(MainWindow.eventHandler)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ControlBay.setTitle(_translate("MainWindow", "Controls"))
        self.Plotting.setTitle(_translate("MainWindow", "Plotting"))
        self.label_2.setText(_translate("MainWindow", "Sampling (Hz)"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.Logging.setTitle(_translate("MainWindow", "Logging"))
        self.label_3.setText(_translate("MainWindow", "Filename"))
        self.filename.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">data\\test.csv</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Enable"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
