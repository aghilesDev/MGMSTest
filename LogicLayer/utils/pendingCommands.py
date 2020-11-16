from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import copy


class PendingCommandsSignal(QObject):
    dataAdded = pyqtSignal('PyQt_PyObject')


class PendingCommands(QObject):
    def __init__(self):
        super(PendingCommands, self).__init__()
        self.signals = PendingCommandsSignal()
        self._values = []
        self.signals.dataAdded.connect(self.on_data_added)

    def moveToThread(self, thread: 'QThread') -> None:
        super(PendingCommands, self).moveToThread(thread)
        self.signals.moveToThread(thread)

    @pyqtSlot('PyQt_PyObject')
    def on_data_added(self, data):
        print("YES")
        print(data)
        self._values.append(data)

    def get_values(self):
        return self._values


def send_signal(signal, data):
    print("here")
    data_to_send = copy.deepcopy(data)
    signal.emit(data_to_send)
