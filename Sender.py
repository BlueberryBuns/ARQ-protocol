import random


class Sender:
    def __init__(self):
        self.data = []
        self.sentData = []
        self.receivedAck = None
        self.packetSize = 8

    def makeData(self):
        for i in range(self.packetSize):
            self.sentData.append(random.randint(0, 1))

    def SendData(self, Dis):
        Dis.dataSendBySender = self.sentData

    def printData(self):
        b = 0
        for i in ["Wysłany pakiet:  " + str(i) for i in self.sentData]:
            print(i, b)
            b += 1
