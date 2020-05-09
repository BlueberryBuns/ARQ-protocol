import random


class Dis:
    def __init__(self):
        self.dataSendBySender = []
        self.dataReceivedByReceiver = []
        self.dataSendByReceiver = []
        self.dataReceivedBySender = []
        self.errorProbabilityMsg = 100
        self.singleDigitErrorProb = 90
        self.errorDrawMsg = None
        self.singleDigitErrorDraw = None

    '''
    def msgDataChangeBool(self):
        if self.errorProbabilityMsg / 100 < self.errorDrawMsg:
            return True
        return False

    def ackDataChangeBool(self):
        if self.singleDigitErrorProb / 100 < self.singleDigitErrorDraw:
            return True
        return False
    '''

    def distortPacket(self, sender):
        self.dataReceivedByReceiver.clear()
        for i in range(len(sender.sentData)):
            self.drawSingleDigitError()
            if self.singleDigitErrorProb / 100 < self.singleDigitErrorDraw:
                self.dataReceivedByReceiver.append(random.randint(0, 1))
            else:
                self.dataReceivedByReceiver.append(self.dataSendBySender[i])
    '''def distortAck(self):
        if self.ackDataChangeBool():  # Jaki kod ma w ogóle ACK ;-;
            pass
    '''

    '''To też już skończone '''

    def passToSender(self, sender):
        sender.receivedAck = self.dataReceivedBySender

    def passToReceiver(self, receiver):
        receiver.receivedData = self.dataReceivedByReceiver

    '''Losowańsko jest tutaj zagrywane'''

    def drawErrorMsg(self):
        self.errorDrawMsg = random.random()

    def drawSingleDigitError(self):
        self.singleDigitErrorDraw = random.random()

    def drukuj(self):
        print("Dane otrzymane przez receiver: ")
        print(self.dataReceivedByReceiver)
