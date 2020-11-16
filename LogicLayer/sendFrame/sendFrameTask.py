from PyQt5.QtCore import QRunnable
from dataclasses import dataclass

class SendFrameTask(QRunnable):
    def __init__(self, data, controller_repository, pending_commands, send_signal):
        super(SendFrameTask, self).__init__()
        self.controller_repository = controller_repository
        self.data = data
        self.pending_commands = pending_commands
        self.send_signal=send_signal

    def run(self) -> None:
        self.controller_repository.signals.write_data.emit(self.data)
        test = Test("hello")
        print("see: {}".format(test))
        self.send_signal(self.pending_commands.signals.dataAdded, test)
        test.name = "Hi"
        test.info.age = 10
        print(test)


@dataclass()
class Info:
    age: int = 30


@dataclass()
class Test:
    name: str = "pergamon"
    info: Info=None

    def __post_init__(self):
        if self.info is None:
            self.info = Info(20)


