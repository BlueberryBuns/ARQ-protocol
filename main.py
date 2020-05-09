from Dis import Dis
from Receiver import Receiver
from Sender import Sender

s1 = Sender()
d1 = Dis()
r1 = Receiver()
#'''
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
#'''
# parityBit
'''
s1.makeData()
s1.encodeParity()
s1.updateData()
s1.printData()
s1.SendData(d1)
d1.drawErrorMsg()
d1.drawSingleDigitError()
d1.distortPacket(s1)
d1.drukuj()
d1.passToReceiver(r1)
r1.decodeParityData(s1)
r1.drukuj()
print(s1.receivedAck)
'''
