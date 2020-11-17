from dependency_injector import containers, providers
from setup import config
from PyQt5.QtCore import QThreadPool
from View.MainView.mainUI import MainUI
from Logic.utils.receptionHandler import ReceptionHandler
from Logic.utils.pendingCommands import PendingCommands, send_signal
from Logic.sendFrame.sendFrameTask import SendFrameTask
from Controller.controllerRepository import ControllerRepository
from View.uiRepository import UIRepository
from Logic.MThread import MThread


class Container(containers.DeclarativeContainer):
    receptionThread = providers.Singleton(MThread)
    pendingCommands = providers.Singleton(PendingCommands)
    threadPool = providers.Singleton(QThreadPool)
    uiRepository = providers.Singleton(UIRepository)
    controllerRepository = providers.Singleton(ControllerRepository,
                                               serial_path=config['SERIAL_PATH'], baud_rate=config['BAUD_RATE'])
    receptionHandler = providers.Singleton(ReceptionHandler, controller_repository=controllerRepository,
                                           ui_repository=uiRepository, pending_commands=pendingCommands)
    sendFrameTask = providers.Factory(SendFrameTask, controller_repository=controllerRepository,
                                      pending_commands=pendingCommands, send_signal=send_signal)
    mainUI = providers.Factory(MainUI, ui_path=config['MAIN_UI_PATH'], send_frame_task=sendFrameTask.provider, ui_repository=uiRepository, thread_pool=threadPool, )