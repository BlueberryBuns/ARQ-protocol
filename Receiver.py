import copy

from Sender import div2mod
from Sender import xor


def div2mod2(divisor, divider):
    dividerLength = len(divider)
    temporary = divisor[0:dividerLength]
    tmp3 = []
    for i in range(dividerLength):
        tmp3.append(0)
    print(tmp3)
    while dividerLength < len(divisor):
        if temporary[0] == 1:
            tmp2 = temporary
            print("temporary2: ")
            print(tmp2)
            print(divider)
            temporary = xor(tmp2, divider)
            print(temporary)
            temporary.append(divisor[dividerLength])
            print("emp after append:")
            print(temporary)
            temporary.pop(0)
            dividerLength += 1
        else:
            tmp2 = temporary
            print("temporary2: ")
            print(tmp2)
            print(tmp3)
            temporary = xor(tmp2, tmp3)
            print(temporary)
            temporary.append(divisor[dividerLength])
            print("emp after append:")
            temporary.pop(0)
            dividerLength += 1
    print(temporary)
    if temporary[0] == 1:
        tmp2 = temporary
        temporary = xor(tmp2, divider)
    else:
        tmp2 = temporary
        temporary = xor(tmp2, tmp3)
    temporary.pop(0)
    print("XD")
    print(temporary)
    return temporary


class Receiver:
    def __init__(self):
        self.completeData = []
        self.receivedData = []
        self.ackMessage = False
        self.key = [1, 0, 1, 1]

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
        parityBit = self.receivedData[len(self.receivedData) - 1]
        self.receivedData.pop((len(self.receivedData) - 1))
        if sum(self.receivedData) % 2 == parityBit:
            self.ackMessage = True
        else:
            self.ackMessage = False

    def decodeCRC(self):
        xd = div2mod2(self.receivedData, self.key)
        checksum = copy.copy(xd)
        print("aaaaaaaaaaaaaaaaa")
        print(checksum)
