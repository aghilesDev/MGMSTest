from PyQt5 import QtSerialPort

config = {
    # UI PATH
    'MAIN_UI_PATH': 'ViewLayer/MainView/main.ui',
    # Serial port Configuration
    'BAUD_RATE': QtSerialPort.QSerialPort.Baud115200,
    'SERIAL_PATH': "/dev/pts/2"
    }
