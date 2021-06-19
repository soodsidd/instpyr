# Imports
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib as mpl

# Ensure using PyQt5 backend
mpl.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.margins(x=0)
        self.ax.minorticks_on()
        self.ax.grid(b=True, which='major', color='silver', linestyle='-')
        self.ax.grid(b=True, which='minor', color='gainsboro', linestyle='--')
        self.fig.tight_layout()
        self.fig.set_tight_layout(True)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.fig.canvas.mpl_connect('button_press_event',lambda event: self.btnpress(event))
        Canvas.updateGeometry(self)
# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    auto_scale=pyqtSignal(int,name='auto_scale')
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.toolbar=myNavToolbar(self.canvas,self)
        # self.toolbar.actions()[3].triggered.connect(self.btpress)
        self.toolbar.autoscale.connect(self.toolbar_active)
        # self.toolbar.canvas.mpl_connect('button_press_event',lambda event: self.btpress(event))
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.toolbar)# Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def toolbar_active(self,active):
        print('nav pressed')
        #pass the signal onto the plotter class
        self.auto_scale.emit(active)

class myNavToolbar(NavigationToolbar):
    autoscale = pyqtSignal(int, name='disautoscale')
    NavigationToolbar.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        #('Back', 'Back to previous view', 'back', 'back'),
        #('Forward', 'Forward to next view', 'forward', 'forward'),
        #(None, None, None, None),
        ('Pan',
         'Left button pans, Right button zooms\n'
         'x/y fixes axis, CTRL fixes aspect',
         'move', 'pan'),
        ('Zoom', 'Zoom to rectangle\nx/y fixes axis, CTRL fixes aspect',
         'zoom_to_rect', 'zoom'),
        #('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
        #(None, None, None, None),
        ('Save', 'Save the figure', 'filesave', 'save_figure'),
      )

    def __init__(self, *args,**kwargs):
        super(myNavToolbar,self).__init__(*args,*kwargs)

    def _update_buttons_checked(self):
        if 'pan' in self._actions:
            self._actions['pan'].setChecked(self.mode.name == 'PAN')

        if 'zoom' in self._actions:
            self._actions['zoom'].setChecked(self.mode.name == 'ZOOM')

        if self.mode.name=='PAN' or self.mode.name=='ZOOM':
            self.autoscale.emit(1)
        else:
            self.autoscale.emit(0)


