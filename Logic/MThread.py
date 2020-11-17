from PyQt5.QtCore import pyqtSlot,pyqtSignal,QObject
from PyQt5.QtCore import QThread


class ThreadSignals(QObject):
    aboutToStop = pyqtSignal()


class MThread(QThread):
    def __init__(self):
        super(MThread, self).__init__()
        self.signals = ThreadSignals()

    def run(self):
        print("Start")
        self.exec()

    @pyqtSlot()
    def quit(self) -> None:
        #self.signals.aboutToStop.emit()
        super(MThread, self).quit()
        print("quit")



