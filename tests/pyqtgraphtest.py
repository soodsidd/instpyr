import sys
import time
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
from time import sleep


class App(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        #### Create Gui Elements ###########
        self.mainbox = QtGui.QWidget()
        self.setCentralWidget(self.mainbox)
        self.mainbox.setLayout(QtGui.QVBoxLayout())

        self.canvas = pg.GraphicsLayoutWidget()
        self.mainbox.layout().addWidget(self.canvas)

        self.label = QtGui.QLabel()
        self.mainbox.layout().addWidget(self.label)

        self.view = self.canvas.addViewBox()
        self.view.setAspectLocked(True)
        self.view.setRange(QtCore.QRectF(0,0, 100, 100))

        #  image plot
        self.img = pg.ImageItem(border='w')
        self.view.addItem(self.img)

        self.canvas.nextRow()
        #  line plot
        self.otherplot = self.canvas.addPlot()
        #this is the widget
        self.otherplot.addLegend()

        self.h2 = self.otherplot.plot(pen='y',name='max')
        self.h3 = self.otherplot.plot(pen='r',name='min')



        #### Set Data  #####################

        self.x = np.linspace(0,50., num=100)
        self.X,self.Y = np.meshgrid(self.x,self.x)

        self.counter = 0
        self.fps = 0.
        self.lastupdate = time.time()

        #### Start  #####################
        self._update()

    def _update(self):
        now = time.time()
        dt = (now - self.lastupdate)
        if dt <= 0:
            dt = 0.000000000001
        elif dt>0.0046:
        # self.data = np.sin(self.X/3.+self.counter/900.)*np.cos(self.Y/3.+self.counter/900.)
            self.ydata = np.sin(self.x/3.+ self.counter*20.)+np.sin(self.x/2.+ self.counter*20)+2
            self.ydata2=np.sin(self.x/3.+ self.counter*20)+2
            # self.ydata.legend.items[0].setText('Name')
            # self.img.setImage(self.data)
            self.h2.setData(x=self.x,y=self.ydata)
            self.h3.setData(x=self.x,y=self.ydata2)
            self.h3.clear()



            self.lastupdate = now
            fps2 = 1.0 / dt
            self.fps = self.fps * 0.9 + fps2 * 0.1
            tx = 'Mean Frame Rate:  {fps:.3f} FPS'.format(fps=self.fps )
            self.label.setText(tx)
            self.counter += 1
        QtCore.QTimer.singleShot(1, self._update)



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    thisapp = App()
    thisapp.show()
    sys.exit(app.exec_())

