from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QThreadPool
from PyQt5 import uic

class MainUI(QtWidgets.QDialog):

    def __init__(self, ui_path, ui_repository, thread_pool: QThreadPool, send_frame_task):
        super(MainUI, self).__init__()
        uic.loadUi(ui_path, self)
        self.show()
        # Bind view component
        self.text = self.findChild(QtWidgets.QLabel, 'label')
        self.frame = self.findChild(QtWidgets.QFrame, 'frameLabel')
        self.data_input = self.findChild(QtWidgets.QLineEdit, 'inputFrame')
        self.button = self.findChild(QtWidgets.QPushButton, 'sendFrameButton')
        # Init Logic
        self.thread_pool = thread_pool
        self.send_frame_task = send_frame_task
        self.ui_repository = ui_repository
        self.button.clicked.connect(self.send_frame)
        self.ui_repository.data_received.connect(self.on_data_received)
        #self.reception_handler.data_received.connect(self.on_data_received)

    @pyqtSlot(str)
    def on_data_received(self, data):
        self.text.setText(data)

    @pyqtSlot()
    def send_frame(self):
        data = self.data_input.text()
        self.thread_pool.start(self.send_frame_task(data))
