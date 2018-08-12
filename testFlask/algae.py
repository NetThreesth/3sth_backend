from allthingstalk import Client, Device, StringAsset, Asset
import time
from threading import Thread

class algaeData(object):
    def __init__(self):
        self.basePump = 0
        self.baseLed = 0
        self.pump = 0
        self.led = 0
        self.density = 0
        self.color = [0, 0, 0]

class algaeDevice(Device):
    PUMP_LED = StringAsset(kind=Asset.VIRTUAL)
    COLOR_DENSITY = StringAsset(kind=Asset.VIRTUAL)
    BASELINE = StringAsset(kind=Asset.VIRTUAL)

class algaeATT(object):
    
    def checkTimer(self, delta):
        if self.__timer > 0:
            self.__timer -= delta
            if self.__timer <= 0:
                self.backToBaseline()

    def updateBaseline(self, newPump, newLed):
        self.__data.baseLed = newLed
        self.__data.basePump = newPump

        ###Update to ATT
        updateAlgae = {
            "led":newLed,
            "pump":newPump
        }
        self.__device.BASELINE = updateAlgae


    def backToBaseline(self):
        self.__data.led = self.__data.baseLed
        self.__data.pump = self.__data.basePump

        ###Update to ATT
        updateAlgae = {
            "led":self.__data.led,
            "pump":self.__data.pump
        }
        self.__device.PUMP_LED = updateAlgae

    def addAlageData(self, pumpVal, ledVal):
        newPump = self.__data.pump + pumpVal;
        newLed = self.__data.led + ledVal;

        newPump = max(0, min(255, newPump))
        newLed = max(0, min(255, newLed))

        self.__data.led = newLed
        self.__data.pump = newPump
        self.__timer = 600

        ###Update to ATT
        updateAlgae = {
            "led":newLed,
            "pump":newPump
        }
        self.__device.PUMP_LED = updateAlgae

    def getAlgaeData(self):
        control = self.__device.PUMP_LED.value
        info = self.__device.COLOR_DENSITY.value
        baseline = self.__device.BASELINE.value
        self.__data.led = control["led"]
        self.__data.pump = control["pump"]
        self.__data.density = info["density"]
        self.__data.color = info["color"]
        self.__data.baseLed = baseline["led"]
        self.__data.basePump = baseline["pump"]


        return self.__data
        

    def __init__(self, deviceId, deviceToken):
        self.__client = Client(deviceToken)
        self.__data = algaeData()
        self.__device = algaeDevice(client = self.__client, id=deviceId)
        self.__timer = 0


