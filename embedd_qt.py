from PyQt5 import QtCore, QtGui, QtWidgets
import r2100_visualize as vr

class MyClass(object):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = PYQTMainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        ...
        self.connect(self.ui.myButton, QtCore.SIGNAL('clicked()'), self.DisplayGraph)
        #next line will work too:
        self.ui.myButton.clicked(self.DisplayGraph)

    def DisplayGraph(self):
        #... set your graph here the way you want
        vr.main(True)
        