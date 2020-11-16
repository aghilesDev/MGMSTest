from PyQt5.QtCore import QObject, pyqtSignal


class UIRepository(QObject):
    data_received = pyqtSignal(str)
