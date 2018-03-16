from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import sys
import random

class Plot2D():
    def __init__(self):
        self.traces = dict()

        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QtGui.QApplication([])
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win.resize(1000,600)
        self.win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        self.canvas = self.win.addPlot(title="Pytelemetry")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def trace(self,name,dataset_x,dataset_y):
        self.canvas.clear()

        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen=pg.mkPen('b', width=5))

    def error(self,name,dataset_x,dataset_y):
        bg1 = pg.BarGraphItem(x=dataset_x, y= 0, height=dataset_y, width=1, brush='#FF0000FF')
        self.canvas.addItem(bg1)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    p = Plot2D()
    performance = []
    time = []
    error = []
    def update():
        global p, performance, time, error
        random_value = random.randrange(7,10)

        if len(performance)<30:
            performance.append(random_value)

            if random_value==8:
                error.append(random_value)
            else:
                error.append(0)
            time = list(range(0,len(performance)))

        else:
            performance = performance[::-1]
            performance.pop()
            performance = performance[::-1]

            error = error[::-1]
            error.pop()
            error = error[::-1]

            performance.append(random_value)
            if random_value==9:
                error.append(random_value)
            else:
                error.append(0)
            time = list(range(0,30))

        print(error)

        p.trace("performance",time,performance)
        p.error("error",time,error)


    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1000)

    p.start()
