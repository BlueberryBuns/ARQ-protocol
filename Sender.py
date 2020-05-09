import random
import copy


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
    print(temporary)
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
            print(temporary)
            temporary.pop(0)
            dividerLength += 1
    print("Juz nic wiecej sie nie dzieje")
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


class Sender:
    def __init__(self):
        self.data = []
        self.sentData = []
        self.key = [0]
        self.receivedAck = None
        self.packetSize = None
        self.pS = 4
        self.encoding = None
        self.test = xor(self.data, self.sentData)
        print(self.test)

    def iterateAndFIll(self):
        i = 0

    def keyUpdate(self, receiver):
        self.key.clear()
        newKey = input("Wprowadź klucz: ")
        for i in range(len(newKey)):
            self.key.append(int(newKey[i]))
        receiver.key = self.key
        print(self.key)
        print(receiver.key)
        print("klucz sendera i receivera")

    def updateData(self):
        self.packetSize = len(self.sentData) + len(self.key) - 1

    def makeData(self):
        for i in range(self.pS):
            self.data.append(random.randint(0, 1))
        print(self.data)

    def SendData(self, Dis):
        Dis.dataSendBySender = self.sentData

    def printData(self):
        print("Wysłane dane: ")
        print(self.sentData)

    def encodeCRC(self):
        self.encoding = "C"
        tmp = copy.deepcopy(self.data)
        for i in range(len(self.key) - 1):
            tmp.append(0)
        print(self.data)
        self.sentData = copy.deepcopy(self.data)
        print("tmp DATA")
        print(tmp)
        self.sentData.extend(div2mod(tmp, self.key))
        print(self.sentData)
        print("XD1")
        pass

    def encodeParity(self):
        self.encoding = "P"
        self.sentData = copy.deepcopy(self.data)

        if sum(self.data) % 2 == 0:
            self.sentData.append(0)
        else:
            self.sentData.append(1)
        print("Patrity Dane:")
        print(self.sentData)
