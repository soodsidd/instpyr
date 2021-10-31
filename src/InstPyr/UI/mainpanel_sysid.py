# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpanel_sysid.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .CustomWidgets.mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 857)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../TemperatureLogger/img/temperature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Sysmodel = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Sysmodel.sizePolicy().hasHeightForWidth())
        self.Sysmodel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sysmodel.setFont(font)
        self.Sysmodel.setObjectName("Sysmodel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Sysmodel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.Sysmodel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.filename = QtWidgets.QTextEdit(self.Sysmodel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.filename.setFont(font)
        self.filename.setObjectName("filename")
        self.verticalLayout.addWidget(self.filename)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.loadModel = QtWidgets.QPushButton(self.Sysmodel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.loadModel.setFont(font)
        self.loadModel.setObjectName("loadModel")
        self.verticalLayout_2.addWidget(self.loadModel)
        self.verticalLayout_8.addWidget(self.Sysmodel)
        self.ModelFit = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ModelFit.sizePolicy().hasHeightForWidth())
        self.ModelFit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ModelFit.setFont(font)
        self.ModelFit.setObjectName("ModelFit")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ModelFit)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.modelselect = QtWidgets.QComboBox(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.modelselect.setFont(font)
        self.modelselect.setObjectName("modelselect")
        self.modelselect.addItem("")
        self.modelselect.addItem("")
        self.verticalLayout_4.addWidget(self.modelselect)
        self.secondOrderParams = QtWidgets.QGroupBox(self.ModelFit)
        self.secondOrderParams.setTitle("")
        self.secondOrderParams.setObjectName("secondOrderParams")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.secondOrderParams)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.secondOrderParams)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.secondOrderParams)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.secondOrderParams)
        self.CuveFit = QtWidgets.QPushButton(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CuveFit.setFont(font)
        self.CuveFit.setObjectName("CuveFit")
        self.verticalLayout_4.addWidget(self.CuveFit)
        self.firstOrderModel = QtWidgets.QGroupBox(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstOrderModel.setFont(font)
        self.firstOrderModel.setObjectName("firstOrderModel")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.firstOrderModel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.firstOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.K_fo = QtWidgets.QLabel(self.firstOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.K_fo.setFont(font)
        self.K_fo.setObjectName("K_fo")
        self.horizontalLayout_6.addWidget(self.K_fo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.firstOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Tau = QtWidgets.QLabel(self.firstOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tau.setFont(font)
        self.Tau.setObjectName("Tau")
        self.horizontalLayout_7.addWidget(self.Tau)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.firstOrderModel)
        self.secondOrderModel = QtWidgets.QGroupBox(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secondOrderModel.setFont(font)
        self.secondOrderModel.setObjectName("secondOrderModel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.secondOrderModel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.K_so = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.K_so.setFont(font)
        self.K_so.setObjectName("K_so")
        self.horizontalLayout_9.addWidget(self.K_so)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.T1_so = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.T1_so.setFont(font)
        self.T1_so.setObjectName("T1_so")
        self.horizontalLayout_10.addWidget(self.T1_so)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.T2_so = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.T2_so.setFont(font)
        self.T2_so.setObjectName("T2_so")
        self.horizontalLayout_16.addWidget(self.T2_so)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.T3_so = QtWidgets.QLabel(self.secondOrderModel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.T3_so.setFont(font)
        self.T3_so.setObjectName("T3_so")
        self.horizontalLayout_8.addWidget(self.T3_so)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.secondOrderModel)
        self.TransferFunc = QtWidgets.QGroupBox(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TransferFunc.setFont(font)
        self.TransferFunc.setObjectName("TransferFunc")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.TransferFunc)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.TransferFunc)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.Tf_num = QtWidgets.QLabel(self.TransferFunc)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tf_num.setFont(font)
        self.Tf_num.setObjectName("Tf_num")
        self.horizontalLayout_12.addWidget(self.Tf_num)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.TransferFunc)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.Tf_den = QtWidgets.QLabel(self.TransferFunc)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tf_den.setFont(font)
        self.Tf_den.setObjectName("Tf_den")
        self.horizontalLayout_11.addWidget(self.Tf_den)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addWidget(self.TransferFunc)
        self.groupBox = QtWidgets.QGroupBox(self.ModelFit)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_8.addWidget(self.ModelFit)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.statusbar_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.statusbar_2.sizePolicy().hasHeightForWidth())
        self.statusbar_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusbar_2.setFont(font)
        self.statusbar_2.setText("")
        self.statusbar_2.setObjectName("statusbar_2")
        self.horizontalLayout_4.addWidget(self.statusbar_2)
        self.plot = MplWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName("plot")
        self.horizontalLayout_4.addWidget(self.plot)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.loadModel.clicked.connect(MainWindow.eventHandler)
        self.modelselect.currentIndexChanged['int'].connect(MainWindow.eventHandler)
        self.CuveFit.clicked.connect(MainWindow.eventHandler)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Identifier"))
        self.Sysmodel.setTitle(_translate("MainWindow", "System Model"))
        self.label_3.setText(_translate("MainWindow", "Filename"))
        self.filename.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">data\\test.csv</p></body></html>"))
        self.loadModel.setText(_translate("MainWindow", "Load Model"))
        self.ModelFit.setTitle(_translate("MainWindow", "ModelFit"))
        self.modelselect.setItemText(0, _translate("MainWindow", "First Order"))
        self.modelselect.setItemText(1, _translate("MainWindow", "Second Order"))
        self.label.setText(_translate("MainWindow", "Max Dyn Ratio"))
        self.CuveFit.setText(_translate("MainWindow", "Fit"))
        self.firstOrderModel.setTitle(_translate("MainWindow", "First Order Model"))
        self.label_5.setText(_translate("MainWindow", "K"))
        self.K_fo.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Tau"))
        self.Tau.setText(_translate("MainWindow", "0"))
        self.secondOrderModel.setTitle(_translate("MainWindow", "Second Order Model"))
        self.label_8.setText(_translate("MainWindow", "K"))
        self.K_so.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "T1"))
        self.T1_so.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "T2"))
        self.T2_so.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "T3"))
        self.T3_so.setText(_translate("MainWindow", "0"))
        self.TransferFunc.setTitle(_translate("MainWindow", "Transfer Function"))
        self.label_11.setText(_translate("MainWindow", "Num"))
        self.Tf_num.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Den"))
        self.Tf_den.setText(_translate("MainWindow", "0"))
        self.groupBox.setTitle(_translate("MainWindow", "Fit Quality"))
        self.label_2.setText(_translate("MainWindow", "Residuals"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
