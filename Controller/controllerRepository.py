from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QIODevice, QTimer
from Controller.mappers import map_baud_rate
from PyQt5 import QtSerialPort


class ControllerRepositorySignal(QObject):
    read_data = pyqtSignal(str)
    write_data = pyqtSignal(str)
    open = pyqtSignal()
    close = pyqtSignal()


class ControllerRepository(QObject):
    def __init__(self, serial_path, baud_rate: QtSerialPort.QSerialPort.BaudRate):
        super(ControllerRepository, self).__init__()
        baud = map_baud_rate(baud_rate)
        self.serial = QtSerialPort.QSerialPort(serial_path, baudRate=baud, readyRead=self.on_data_read)
        self.signals = ControllerRepositorySignal()
        self.serial.errorOccurred.connect(self.error)
        self.signals.write_data.connect(self.on_write_data)
        self.isOpen = False
        self.signals.open.connect(self.on_open)
        self.signals.close.connect(self.on_close)

    def moveToThread(self, thread: 'QThread') -> None:
        super(ControllerRepository, self).moveToThread(thread)
        self.serial.moveToThread(thread)
        self.signals.moveToThread(thread)

    @pyqtSlot()
    def on_open(self):
        if not self.serial.open(QIODevice.ReadWrite):
            QTimer.singleShot(3000, self.on_open)
            print("error")
        else:
            self.isOpen = False

    @pyqtSlot()
    def on_close(self):
        self.serial.close()

    @pyqtSlot(QtSerialPort.QSerialPort.SerialPortError)
    def error(self, data: int):
        if (data == 9 or data == 8 or data == 1) and self.isOpen:
            print("ERROR occurred: {}".format(data))
            self.isOpen = False
            self.serial.close()
            self.connect()

    @pyqtSlot(str)
    def on_write_data(self, data):
        print("write data: {}".format(data))
        self.serial.write(data.encode())

    @pyqtSlot()
    def on_data_read(self):
        print("maybe here")
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.signals.read_data.emit(text)
