import random


def xor(a, b):
    result = []
    for i in range(len(b)):
        if a[i] == b[i]:
            result.append(0)
        else:
            result.append(1)
    return result


def div2mod(divisor, divider):
    dividerLength = len(divider)
    temporary = divisor[0:dividerLength]
    tmp3 = []
    for i in range(dividerLength):
        tmp3.append(0)
    print(tmp3)
    while dividerLength < len(divisor):
        if temporary[0] == 1:
            tmp2 = temporary
            temporary = xor(tmp2, divider)
            print(temporary)
            temporary.append(divisor[dividerLength])
            temporary.pop(0)
            dividerLength += 1
        else:
            tmp2 = temporary
            temporary = xor(tmp2, tmp3)
            temporary.append(divisor[dividerLength])
            temporary.pop(0)
            dividerLength += 1
    print(temporary)
    print("XD")

class Sender:
    def __init__(self):
        self.data = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0]
        self.sentData = [1, 0, 1, 1]
        self.receivedAck = None
        self.packetSize = 8
        self.encoding = None
        self.test = xor(self.data, self.sentData)
        print(self.test)
        div2mod(self.data,self.sentData)

    def makeData(self):
        for i in range(self.packetSize):
            self.sentData.append(random.randint(0, 1))

    def SendData(self, Dis):
        Dis.dataSendBySender = self.sentData

    def printData(self):
        b = 0
        print("Wysłane dane: ")
        print(self.sentData)

    def encodeCRC(self):
        self.encoding = "CRC"
        pass

    def encodeParity(self):
        self.encoding = "Parity"
        for i in self.data:
            if sum(self.data) % 2 == 0:
                self.data.append(0)
            else:
                self.data.append(1)
                self.data.append(1)
