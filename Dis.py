import random


class Dis:
    def __init__(self):
        self.dataSendBySender = []
        self.dataReceivedByReceiver = []
        self.dataSendByReceiver = []
        self.dataReceivedBySender = []
        self.errorProbabilityMsg = 0
        self.singleDigitErrorProb = 0
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

    def distortPacket(self, Sender):
        for i in range(Sender.packetSize):
            self.drawSingleDigitError()
            if self.singleDigitErrorProb / 100 < self.singleDigitErrorDraw:
                self.dataReceivedByReceiver.append(random.randint(0, 1))
            else:
                self.dataReceivedByReceiver.append(self.dataSendBySender[i])

    def distortAck(self):
        if self.ackDataChangeBool():  # Jaki kod ma w ogóle ACK ;-;
            pass
    '''To też już skończone '''
    def passToSender(self, Sender):
        Sender.receivedAck = self.dataReceivedBySender

    def passToReceiver(self, Receiver):
        Receiver.receivedData = self.dataReceivedByReceiver

    '''Losowańsko jest tutaj zagrywane'''

    def drawErrorMsg(self):
        self.errorDrawMsg = random.random()

    def drawSingleDigitError(self):
        self.singleDigitErrorDraw = random.random()

    def drukuj(self):
        a = 0
        for i in ["Pakiet po zmianie:  " + str(i) for i in self.dataReceivedByReceiver]:
            print(i, a)
            a += 1