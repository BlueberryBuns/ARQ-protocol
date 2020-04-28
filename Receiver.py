class Receiver:
    def __init__(self):
        self.completeData = []
        self.receivedData = []
        self.ackMessage = False

    def decodeData(self):
        pass

    def sendAck(self, Dis):
        Dis.dataSendByReceiver = self.ackMessage

    def drukuj(self):
        a = 0
        for i in ["Pakiet po zmianie:  " + str(i) for i in self.receivedData]:
            print(i, a)
            a += 1

    def decodeParityData(self):
        parityBit = self.receivedData(len(self.receivedData)-1)
        self.receivedData.pop((len(self.receivedData) - 1))
        if sum(self.receivedData) % 2 == parityBit:
            self.ackMessage = True
        else:
             self.ackMessage = False