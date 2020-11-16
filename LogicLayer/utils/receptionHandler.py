from PyQt5.QtCore import QObject,pyqtSlot


class ReceptionHandler(QObject):
    def __init__(self, controller_repository, ui_repository, pending_commands):
        super(ReceptionHandler, self).__init__()
        self.controller_repository = controller_repository
        self.ui_repository = ui_repository
        self.controller_repository.signals.read_data.connect(self.on_read_data)
        self.pending_commands = pending_commands



    @pyqtSlot(str)
    def on_read_data(self, data):
        print(data)
        self.ui_repository.data_received.emit(data)
        print(self.pending_commands.get_values())


