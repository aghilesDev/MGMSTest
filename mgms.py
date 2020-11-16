from injection import Container
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    # Create an instance of QtWidgets.QApplication
    container = Container()
    app = QtWidgets.QApplication(sys.argv)

    # initialize threads
    reception_thread = container.receptionThread()

    # initialize objects
    window = container.mainUI()
    controller_repo = container.controllerRepository()
    receiver_handler = container.receptionHandler()
    pending_commands = container.pendingCommands()

    # launch threads
    reception_thread.start()

    # moving object to their respective threads

    receiver_handler.moveToThread(reception_thread)
    controller_repo.moveToThread(reception_thread)
    pending_commands.moveToThread(reception_thread)

    controller_repo.signals.open.emit()

    app.exec_() # Start the application

class MGMS:
    def __init__(self):
        # Create an instance of QtWidgets.QApplication
        self.container = Container()
        self.app = QtWidgets.QApplication(sys.argv)

        # initialize threads
        self.reception_thread = self.container.receptionThread()

        # initialize objects
        self.window = self.container.mainUI()
        self.controller_repo = self.container.controllerRepository()
        self.receiver_handler = self.container.receptionHandler()
        self.pending_commands = self.container.pendingCommands()

    def execute(self):
        # launch threads
        self.reception_thread.start()

        # moving object to their respective threads

        self.receiver_handler.moveToThread(self.reception_thread)
        self.controller_repo.moveToThread(self.reception_thread)
        self.pending_commands.moveToThread(self.reception_thread)

        self.controller_repo.signals.open.emit()

        self.app.exec_()
