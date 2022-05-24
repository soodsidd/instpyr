from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import numpy as np
# from cycler import cycler
import numpy as np
from ..Utilities.watch import watch
from ..Plotting.pyqtgraphwidget import PyQtGraphWidget
from varname import nameof
linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or ':'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'

pens=['b','g','r','c','m','y','k','w']

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),

     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

class FastPlotter:
    def __init__(self, PlotWidget, variables:list=None, buffersize=10000, initdata=None):
        # setup the plot here- empty data
        #initdata must be a dictionary
        #initialize plotdata objects

        self.lines={}
        self.plotrefs={}
        self.pltdata={}
        self.buffer = buffersize
        self.plotwidget = PlotWidget
        lines = 0  
        self.legend = True
        self.autoscale=True
        self.ylims=[0,0]
        self.xaxis=None
        self.ylines={}

        self.horzoom=buffersize
        #connect plotwidget signals - these are signals from UI interactions with this widget
        self.plotwidget.xvariable_sig.connect(self._xchanged)
        self.plotwidget.yvars_sig.connect(self._yvarschanged)
        self.plotwidget.zoomsig.connect(self._horZoomChanged)



        self.lines['Time']=_linedata('Time',buffersize= buffersize,Xaxis=True,Yaxis=False,timedata=True)

        for item in variables:
            if isinstance(item,watch):
                data=_linedata(item.name,buffersize=buffersize,precision=item.precision,Xaxis=False,Yaxis=True)
                self.lines[item.name]=data
        self.varlist=[x.name for x in variables]
        self.plotwidget.populateVariables(self.varlist)

        self.initplots()




    def initplots(self):
        self.xaxis=None
        self.ylines= {}
        # for ref in self.plotrefs.keys():
        #     self.plotrefs[ref].remove()
        self.plotrefs={}
        self.plotwidget.clear()
        styleindex=0


        #sort lines into x axis lines and y axis lines
        for key in self.lines.keys():
            line=self.lines[key]
            if line.Xaxis:
                self.xaxis=line
            elif line.Yaxis:
                self.ylines[line.name]=line


        #create a ref for each line
        for key in self.ylines.keys():
            line=self.ylines[key]
            plot_ref=self.plotwidget.plot(x=self.xaxis.data,y=line.data,name=line.name,pen=pens[styleindex])
            self.plotrefs[line.name]=plot_ref
            styleindex+=1

        self.plotwidget.addLegend()

        self.legend=True

    def _horZoomChanged(self,params):
        self.horzoom=int(self.buffer*params/100)
        print(params)

    def _xchanged(self,params):
        print(params)
        if self.xaxis is not None:
            if params[1] in self.lines.keys():
                currentx=self.xaxis.name
                self.lines[currentx].Xaxis=False

                self.lines[params[1]].Xaxis=True

        self.initplots()

    def _yvarschanged(self,params):
        print(params)
        yvar=self.varlist[params[0]]
        yvarenable=params[1]
        self.lines[yvar].Yaxis=yvarenable
        self.initplots()



    # @property
    # def legend(self):
    #     return self._legend
    # @legend.setter
    # def legend(self,val):
    #     self._legend=val
    #     if val==False:
    #         if self.plotwidget.canvas.ax.get_legend() is not None:
    #             self.plotwidget.canvas.ax.get_legend().remove()
    #             if self.ax2 is not None:
    #                 if self.ax2.get_legend() is not None:
    #                     self.ax2.get_legend().remove()
    #     else:
    #         leg=self.plotwidget.canvas.ax.legend(loc=3)
    #         if self.ax2 is not None:
    #             # leg.remove()
    #             self.ax2.legend(loc=4)
    #             # self.ax2.add_artist(leg)

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self,val):
        self._buffer=val
        for key in self.lines.keys():
            self.lines[key].buffersize=val


    def updatedata(self,timestamp,watchdata:dict):

        #watch data is a list of sensors
        #data is a dictionary of single point data
        #timestamp is the current datetime
        self.lines['Time'].update(timestamp)
        #TODO concatenate time and watchitem
        if isinstance(watchdata,dict):
            for key in watchdata.keys():
                if key in self.varlist:
                    self.lines[key].update(watchdata[key])

        self._updateplots()



    def _updateplots(self):
        #now that the data has been updated in all _linedata, now update all the plotrefs
        plotlen=len(self.xaxis.data)
        lowind=0 if (plotlen-self.horzoom)<0 else (plotlen-self.horzoom)
        highind=plotlen
        for key in self.plotrefs.keys():
            self.plotrefs[key].setData(x=self.xaxis.data[lowind:highind], y=self.lines[key].data[lowind:highind])
            precision=self.lines[key].precision
            # self.plotrefs[key].set_label(key + ':' + f"{self.lines[key].latestpoint:.2f}")
            # self.legend=True



    def clear(self,key=None):
        for key in self.lines.keys():
            self.lines[key].data=[]
            print('here')





class _linedata:
    def __init__(self,name,buffersize,precision=2,Xaxis=False,Yaxis=True,timedata=False):
        self.name=name
        self.Xaxis=Xaxis
        self.Yaxis=Yaxis
        self.timedata=timedata
        self.precision=precision
        self.data=[]
        self.buffersize=buffersize
        self.latestpoint=0

    def update(self,data):
        self.data.append(data)
        #TODO change this to numpy array
        l=len(self.data)
        if l >self.buffersize:
            self.data=self.data[(l-self.buffersize):l]
        self.latestpoint=data


class _PlotTester(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w=PyQtGraphWidget()

        self.sense1=0
        self.sense2=1
        self.sense3=2
        self.currenttime=0

        watch1=watch('Sense 1',nameof(self.sense1),callfunc=self.variableProbe)
        watch2 = watch('Sense 2', nameof(self.sense2), callfunc=self.variableProbe)
        watch3 = watch('Sense 3', nameof(self.sense3), callfunc=self.variableProbe)
        
        self.watchlist=[watch1,watch2,watch3]
        self.myplot=FastPlotter(self.w, variables=self.watchlist)

        self.setCentralWidget(self.w)
        self.lastupdate=time.time()
        self.updateTestPlot()


    def updateTestPlot(self):
        now=time.time()
        dt=now-self.lastupdate
        self.currenttime+=dt

        self.sense1=105.23-np.random.randint(5)
        self.sense2=80.12-np.random.randint(5)
        self.sense3=111-np.random.randint(10)

        #dictionary of sensor readings:
        data={}
        for watch in self.watchlist:
            data[watch.name]=watch.read()

        self.myplot.updatedata(self.currenttime,data)
        self.lastupdate=now
        QtCore.QTimer.singleShot(1, self.updateTestPlot)



    def variableProbe(self,name):
        return eval('self.'+name)

if __name__=="__main__":
    from mplwidget import MplWidget

    app = QApplication(sys.argv)
    window=_PlotTester()
    window.show()
    app.exec_()


