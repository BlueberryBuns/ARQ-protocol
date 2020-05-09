from Dis import Dis
from Receiver import Receiver
from Sender import Sender

s1 = Sender()
d1 = Dis()
r1 = Receiver()
'''
# CRC coding
s1.makeData()
s1.keyUpdate(r1)
s1.updateData()
s1.encodeCRC()
s1.printData()
s1.SendData(d1)
d1.drawErrorMsg()
d1.drawSingleDigitError()
d1.distortPacket(s1)
d1.drukuj()
d1.passToReceiver(r1)
r1.drukuj()
r1.decodeCRC(s1)
print(s1.receivedAck)
'''
# parityBit
# '''
counterOne = 0
counterTwo = 0
counterOverTwo = 0

for i in range(1000):
    j = 0
    s1.data.clear()
    s1.sentData.clear()
    d1.dataSendBySender.clear()
    d1.dataReceivedByReceiver.clear()
    s1.makeData()
    s1.encodeParity()
    s1.updateData()
    s1.printData()
    while not s1.receivedAck:
        j += 1
        d1.dataReceivedByReceiver.clear()
        s1.SendData(d1)
        d1.drawErrorMsg()
        d1.drawSingleDigitError()
        d1.distortPacket(s1)
        d1.drukuj()
        d1.passToReceiver(r1)
        r1.decodeParityData(s1)
        r1.drukuj()
        print(s1.receivedAck)
    if j == 1:
        counterOne+=1
    elif j ==2:
        counterTwo+=1
    else:
        counterOverTwo+=1

    s1.receivedAck = False
    print("********")

print(counterOne)
print(counterTwo)
print(counterOverTwo)
# '''
# ile pakietow potrzebowalo jednego wyslania
# ile dwoch i ile 3 i więcej
