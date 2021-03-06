# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpanel_autotuner.ui'
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
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Control = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Control.sizePolicy().hasHeightForWidth())
        self.Control.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Control.setFont(font)
        self.Control.setObjectName("Control")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Control)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.Tfnum = QtWidgets.QLineEdit(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tfnum.setFont(font)
        self.Tfnum.setText("")
        self.Tfnum.setObjectName("Tfnum")
        self.verticalLayout_5.addWidget(self.Tfnum)
        self.label_2 = QtWidgets.QLabel(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.Tfden = QtWidgets.QLineEdit(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tfden.setFont(font)
        self.Tfden.setObjectName("Tfden")
        self.verticalLayout_5.addWidget(self.Tfden)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.stepAmp = QtWidgets.QDoubleSpinBox(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.stepAmp.setFont(font)
        self.stepAmp.setProperty("value", 1.0)
        self.stepAmp.setObjectName("stepAmp")
        self.horizontalLayout_8.addWidget(self.stepAmp)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.simDuration = QtWidgets.QDoubleSpinBox(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.simDuration.setFont(font)
        self.simDuration.setMaximum(9999.0)
        self.simDuration.setProperty("value", 30.0)
        self.simDuration.setObjectName("simDuration")
        self.horizontalLayout_9.addWidget(self.simDuration)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.timeSteps = QtWidgets.QSpinBox(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timeSteps.setFont(font)
        self.timeSteps.setMaximum(1000)
        self.timeSteps.setProperty("value", 100)
        self.timeSteps.setObjectName("timeSteps")
        self.horizontalLayout_10.addWidget(self.timeSteps)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.StepResponse = QtWidgets.QPushButton(self.Control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StepResponse.setFont(font)
        self.StepResponse.setObjectName("StepResponse")
        self.verticalLayout_5.addWidget(self.StepResponse)
        self.verticalLayout_8.addWidget(self.Control)
        self.AutotunePM = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AutotunePM.setFont(font)
        self.AutotunePM.setObjectName("AutotunePM")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AutotunePM)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.AutotunePM)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Kc_ini = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Kc_ini.setFont(font)
        self.Kc_ini.setMaximum(9999.0)
        self.Kc_ini.setProperty("value", 1.0)
        self.Kc_ini.setObjectName("Kc_ini")
        self.horizontalLayout_2.addWidget(self.Kc_ini)
        self.Kc_lb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Kc_lb.setFont(font)
        self.Kc_lb.setMinimum(0.0)
        self.Kc_lb.setProperty("value", 0.1)
        self.Kc_lb.setObjectName("Kc_lb")
        self.horizontalLayout_2.addWidget(self.Kc_lb)
        self.Kc_ub = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Kc_ub.setFont(font)
        self.Kc_ub.setMaximum(9999.0)
        self.Kc_ub.setProperty("value", 99.99)
        self.Kc_ub.setObjectName("Kc_ub")
        self.horizontalLayout_2.addWidget(self.Kc_ub)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.Ti_ini = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Ti_ini.setFont(font)
        self.Ti_ini.setMinimum(0.1)
        self.Ti_ini.setMaximum(9999.0)
        self.Ti_ini.setProperty("value", 1.0)
        self.Ti_ini.setObjectName("Ti_ini")
        self.horizontalLayout_3.addWidget(self.Ti_ini)
        self.Ti_lb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Ti_lb.setFont(font)
        self.Ti_lb.setSingleStep(0.1)
        self.Ti_lb.setProperty("value", 0.1)
        self.Ti_lb.setObjectName("Ti_lb")
        self.horizontalLayout_3.addWidget(self.Ti_lb)
        self.Ti_ub = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Ti_ub.setFont(font)
        self.Ti_ub.setMinimum(0.1)
        self.Ti_ub.setMaximum(9999.0)
        self.Ti_ub.setProperty("value", 99.99)
        self.Ti_ub.setObjectName("Ti_ub")
        self.horizontalLayout_3.addWidget(self.Ti_ub)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.Td_ini = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Td_ini.setFont(font)
        self.Td_ini.setMaximum(9999.0)
        self.Td_ini.setProperty("value", 0.1)
        self.Td_ini.setObjectName("Td_ini")
        self.horizontalLayout_6.addWidget(self.Td_ini)
        self.Td_lb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Td_lb.setFont(font)
        self.Td_lb.setProperty("value", 0.1)
        self.Td_lb.setObjectName("Td_lb")
        self.horizontalLayout_6.addWidget(self.Td_lb)
        self.Td_ub = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Td_ub.setFont(font)
        self.Td_ub.setMaximum(9999.0)
        self.Td_ub.setProperty("value", 99.99)
        self.Td_ub.setObjectName("Td_ub")
        self.horizontalLayout_6.addWidget(self.Td_ub)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.AutotunePM)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.out_min = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.out_min.setFont(font)
        self.out_min.setObjectName("out_min")
        self.horizontalLayout_12.addWidget(self.out_min)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.out_max = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.out_max.setFont(font)
        self.out_max.setMaximum(999.99)
        self.out_max.setProperty("value", 999.0)
        self.out_max.setObjectName("out_max")
        self.horizontalLayout_11.addWidget(self.out_max)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.AutotunePM)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_14.addWidget(self.label_17)
        self.riseweight = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.riseweight.setFont(font)
        self.riseweight.setObjectName("riseweight")
        self.horizontalLayout_14.addWidget(self.riseweight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.settlingweight = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.settlingweight.setFont(font)
        self.settlingweight.setObjectName("settlingweight")
        self.horizontalLayout_5.addWidget(self.settlingweight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Simulate = QtWidgets.QPushButton(self.AutotunePM)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Simulate.setFont(font)
        self.Simulate.setObjectName("Simulate")
        self.horizontalLayout_13.addWidget(self.Simulate)
        self.Autotune = QtWidgets.QPushButton(self.AutotunePM)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Autotune.setFont(font)
        self.Autotune.setObjectName("Autotune")
        self.horizontalLayout_13.addWidget(self.Autotune)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addWidget(self.AutotunePM)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Plot1 = MplWidget(self.frame_3)
        self.Plot1.setObjectName("Plot1")
        self.verticalLayout.addWidget(self.Plot1)
        self.Plot2 = MplWidget(self.frame_3)
        self.Plot2.setObjectName("Plot2")
        self.verticalLayout.addWidget(self.Plot2)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.Autotune.clicked.connect(MainWindow.eventHandler)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PID Autotuner"))
        self.Control.setTitle(_translate("MainWindow", "System TF"))
        self.label.setText(_translate("MainWindow", "Numerator"))
        self.Tfnum.setPlaceholderText(_translate("MainWindow", "[1]"))
        self.label_2.setText(_translate("MainWindow", "Denominator"))
        self.Tfden.setPlaceholderText(_translate("MainWindow", "[1,100]"))
        self.label_12.setText(_translate("MainWindow", "Step Amplitude"))
        self.label_13.setText(_translate("MainWindow", "Duration"))
        self.label_14.setText(_translate("MainWindow", "Time steps"))
        self.StepResponse.setText(_translate("MainWindow", "Step Response"))
        self.AutotunePM.setTitle(_translate("MainWindow", "Autotune Settings"))
        self.groupBox_2.setTitle(_translate("MainWindow", "PID parameters"))
        self.label_8.setText(_translate("MainWindow", "Init                "))
        self.label_9.setText(_translate("MainWindow", "LB              "))
        self.label_10.setText(_translate("MainWindow", "UB                "))
        self.label_5.setText(_translate("MainWindow", "Kc"))
        self.label_6.setText(_translate("MainWindow", "Ti"))
        self.label_7.setText(_translate("MainWindow", "Td"))
        self.groupBox.setTitle(_translate("MainWindow", "Saturation"))
        self.label_16.setText(_translate("MainWindow", "Minimum"))
        self.label_15.setText(_translate("MainWindow", "Maximum"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Objective function"))
        self.label_3.setText(_translate("MainWindow", "Overshoot Weight"))
        self.label_17.setText(_translate("MainWindow", "RiseTime Weight"))
        self.label_4.setText(_translate("MainWindow", "Settling Weight"))
        self.Simulate.setText(_translate("MainWindow", "Simulate!"))
        self.Autotune.setText(_translate("MainWindow", "Autotune!"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
