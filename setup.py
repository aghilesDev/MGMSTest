from PyQt5 import QtSerialPort
import json


CONFIG_PATH = "config.json"

data = None

with open("config.json", "r") as file:
    data = json.load(file)

config = {
    }

for key in data:
    config[key] = data[key]


