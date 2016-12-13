#!/usr/bin/env python3

from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
import sys



from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
    
import os
uipath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ui")

Ui_MainWindow, QMainWindow = loadUiType(os.path.join(uipath,'firstorder.ui'))

from scipy import signal

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow2, self).__init__(parent)
        loadUiType(os.path.join(uipath,'firstorder.ui'), self)

class MainWindow3(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow3, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)
                
        self.plotButton.clicked.connect(self.makeplot)
        
    def makeplot(self):
        self.stepplot()
        
    def stepplot(self):
         K = self.gain.value()
         tau = self.tau.value()
         sys = signal.TransferFunction([K],[tau,1])
         T, yout = signal.step(sys)
         self.ax.clear()
         self.ax.plot(T,yout)
         self.canvas.draw()
         self.toolbar
         if self.navTools.isChecked():
             self.verticalLayout.addWidget(self.toolbar)
         else:
             self.verticalLayout.removeWidget(self.toolbar)
         print(self.navTools.isChecked())
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())
