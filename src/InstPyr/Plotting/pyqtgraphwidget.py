# Imports
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import pyqtSignal
import pyqtgraph as pg

class PyQtGraphWidget(QtWidgets.QWidget):
    auto_scale=pyqtSignal(int,name='auto_scale')
    xvariable_sig=pyqtSignal(list,name='xvariable')
    yvars_sig=pyqtSignal(list,name='yvars')
    zoomsig=pyqtSignal(int,name='ZoomSignal')

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = pg.GraphicsLayoutWidget()
        self.plotwidget=self.canvas.addPlot()
        self.yvars=[]

        #Add widgets here:
        self.showVars=QtWidgets.QRadioButton()
        self.Xlabel=QtWidgets.QLabel('X-Axis:')
        self.Ylabel=QtWidgets.QLabel(' Y-Axis:')
        self.Xchoices=QtWidgets.QComboBox()
        self.xaxisdropdown = QtWidgets.QHBoxLayout()
        self.xaxisdropdown.addStretch(1)
        self.xaxisdropdown.addWidget(self.Xlabel)
        self.xaxisdropdown.addWidget(self.Xchoices)
        self.xaxisdropdown.addStretch(1)
        self.variableselector=QtWidgets.QScrollArea()
        self.variableselectorlayout=QtWidgets.QVBoxLayout()
        self.variableselector.setLayout(self.variableselectorlayout)
        self.timezoom=QtWidgets.QSlider()

        #Initialize Widgets here:
        self.showVars.setChecked(False)
        self.variableselector.hide()
        # self._populateYvars(['P gain','Control signal','D gain','G gain','Error','Temperature','Pressure'])
        #Connect signals
        self.showVars.clicked.connect(self._showvarbar)
        self.Xchoices.currentIndexChanged.connect(self._xvarChanged)
        self.timezoom.sliderMoved['int'].connect(self._zoomChanged)


        #Setup Layout
        self._setupLayout()
        self.Xchoices.setCurrentText('Time')

        #TODO add multithreading here
    def plot(self,x,y,name='',pen='r'):
        ref=self.plotwidget.plot(x=x,y=y,name=name,pen=pen)
        return ref

    def addLegend(self):
        self.plotwidget.addLegend()

    def clear(self):
        self.plotwidget.clear()

    def _setupLayout(self):
        self.topbar=QtWidgets.QHBoxLayout()

        showVarSizePol=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        showVarSizePol.setHorizontalStretch(4)

        MainframeSizePol=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        MainframeSizePol.setHorizontalStretch(20)

        comboBoxSize=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Maximum)
        self.Xchoices.setSizePolicy(comboBoxSize)
        self.Xchoices.addItem("Time")
        font=QtGui.QFont()
        font.setPointSize(8)
        self.Xchoices.setFont(font)
        font.setPointSize(8)
        self.Xlabel.setFont(font)
        self.Ylabel.setFont(font)

        self.topbar.addWidget(self.Xlabel)
        self.topbar.addWidget(self.Xchoices)
        # self.topbar.addStretch()
        self.topbar.addWidget(self.Ylabel)
        self.topbar.addWidget(self.showVars)
        self.mainframe=QtWidgets.QFrame()
        self.vbl=QtWidgets.QVBoxLayout(self.mainframe)
        self.vbl.addLayout(self.topbar)
        self.vbl.addWidget(self.canvas)
        self.mainframe.setSizePolicy(MainframeSizePol)
        self.variableselector.setSizePolicy(showVarSizePol)
        self.hbl=QtWidgets.QHBoxLayout()
        self.hbl.addWidget(self.mainframe)
        self.hbl.addWidget(self.timezoom)
        self.hbl.addWidget(self.variableselector)
        self.setLayout(self.hbl)

    def _showvarbar(self):
        if self.showVars.isChecked():
            self.variableselector.show()
        else:
            self.variableselector.hide()

    def populateVariables(self,names):
        header=QtWidgets.QHBoxLayout()
        center=QtWidgets.QLabel('Vars')
        font = QtGui.QFont()
        font.setPointSize(10)
        # font.setBold(True)
        center.setFont(font)
        header.addStretch(1)
        header.addWidget(center)
        header.addStretch(1)
        self.variableselectorlayout.addLayout(header)
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.variableselectorlayout.addWidget(line)
        if isinstance(names, list):
            for elem in names:
                self._addYvar(elem)
        self.variableselectorlayout.addStretch(1)


    def _addYvar(self,name):
        # index=len(self.yvars)
        index=len(self.yvars)
        rowhbox=QtWidgets.QHBoxLayout()
        cboxL=QtWidgets.QCheckBox()
        cboxL.setObjectName(str(index))
        cboxL.setChecked(True)

        cboxL.clicked['bool'].connect(self._yvarChecked)



        label=QtWidgets.QLabel(name)
        font=QtGui.QFont()
        font.setPointSize(8)
        label.setFont(font)
        rowhbox.addWidget(cboxL)
        rowhbox.addStretch(1)
        rowhbox.addWidget(label)
        rowhbox.addStretch(1)
        self.variableselectorlayout.addLayout(rowhbox)
        self.Xchoices.addItem(name)
        self.yvars.append(cboxL)

    def _yvarChecked(self,state,*args):
        index=int(self.sender().objectName())
        self.yvars_sig.emit([index,state])
        print(state)
        print('here')

    def _xvarChanged(self,index,*args):
        print(self.sender().objectName())
        text=self.Xchoices.currentText()
        self.xvariable_sig.emit([index,text])
        # print('here'+str(index))

    def _zoomChanged(self,scale):
        self.zoomsig.emit(scale)





