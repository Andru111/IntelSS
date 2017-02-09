import sys
from PyQt4 import QtGui, QtCore
import pyqtgraph as pq
from kernel import kernel
import scipy as sp

class UI(QtGui.QWidget):

    def __init__(self, camp_dist):
        pq.setConfigOption('background', 'w')
        self.widget = pq.PlotWidget()
        self.kernel = kernel('../data/csv/out.csv', camp_dist)
        self.kernel.pars()
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):

        """cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)"""

        #x = np.random.normal(size=1000)
        x = [1, 2, 423, 234 ,52]
        button1 = QtGui.QPushButton('Open file', self)
        button1.resize(70, 40)
        button1.clicked.connect(self.choseFile)

        button2 = QtGui.QPushButton('Create chart', self)
        button2.resize(70, 40)
        button2.move(0, 50)
        button2.clicked.connect(self.createChart)

        self.setGeometry(30, 30, 790, 720)
        self.setWindowTitle('sosi hui bidlo 1488')
        self.show()

    def choseFile(self):

        arr = QtGui.QFileDialog.getOpenFileName(self)
        file = open(arr, 'r')
        self.full_data = file.read()
        file.close()

    def createChart(self):
        data = self.kernel.comput_first()
        self.widget.plotItem.plot(data, symbol='o')
        self.widget.resize(700, 700)
        self.widget.move(80, 10)
        self.widget.show()



def main(camp_dist):
    app = QtGui.QApplication(sys.argv)
    ex = UI(camp_dist)
    sys.exit(app.exec_())

if __name__ == '__main__':
    camp_dist = sp.genfromtxt('../data/camp_dist.tsv', delimiter='\t')
    main(camp_dist)
