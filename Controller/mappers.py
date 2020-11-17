from PyQt5 import QtSerialPort

mapper = {
    "1200": QtSerialPort.QSerialPort.Baud1200,
    "2400": QtSerialPort.QSerialPort.Baud2400,
    "4800": QtSerialPort.QSerialPort.Baud4800,
    "9600": QtSerialPort.QSerialPort.Baud9600,
    "19200": QtSerialPort.QSerialPort.Baud19200,
    "38400": QtSerialPort.QSerialPort.Baud38400,
    "57600": QtSerialPort.QSerialPort.Baud57600,
    "115200": QtSerialPort.QSerialPort.Baud115200
}


def map_baud_rate(raw_baud_rate):
    baud_rate = mapper[str(raw_baud_rate)]
    if baud_rate is None:
        assert ValueError("Invalid baudRate")
    return baud_rate

