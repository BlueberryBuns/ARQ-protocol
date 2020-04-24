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