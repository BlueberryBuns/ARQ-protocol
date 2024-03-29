import random


class Dis:
    def __init__(self):
        self.dataSendBySender = []
        self.dataReceivedByReceiver = []
        self.dataSendByReceiver = []
        self.dataReceivedBySender = []
        #self.errorProbabilityMsg = 100
        self.singleDigitErrorProb = 3
        self.errorDrawMsg = None
        self.singleDigitErrorDraw = None

    # def distortPacket(self, sender):
    #     self.dataReceivedByReceiver.clear()
    #     for i in range(len(sender.sentData)):
    #         self.drawSingleDigitError()
    #         if self.singleDigitErrorProb / 100 < self.singleDigitErrorDraw:
    #             self.dataReceivedByReceiver.append(random.randint(0, 1))
    #         else:
    #             self.dataReceivedByReceiver.append(self.dataSendBySender[i])

    def distortPacket(self, sender):
        self.dataReceivedByReceiver.clear()
        for i in range(len(sender.sentData)):
            self.drawSingleDigitError()
            if self.singleDigitErrorProb >= random.randint(1,100):
                if self.dataReceivedByReceiver == 1:
                    self.dataReceivedByReceiver.append(0)
                else:
                    self.dataReceivedByReceiver.append(1)
            else:
                self.dataReceivedByReceiver.append(self.dataSendBySender[i])

    def passToSender(self, sender):
        sender.receivedAck = self.dataReceivedBySender

    def passToReceiver(self, receiver):
        receiver.receivedData = self.dataReceivedByReceiver

    def drawErrorMsg(self):
        self.errorDrawMsg = random.random()

    def drawSingleDigitError(self):
        self.singleDigitErrorDraw = random.random()

    def drukuj(self):
        print("Dane otrzymane przez receiver: ")
        print(self.dataReceivedByReceiver)
