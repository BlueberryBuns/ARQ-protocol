from Dis import Dis
from Receiver import Receiver
from Sender import Sender

s1 = Sender()
d1 = Dis()
r1 = Receiver()

s1.makeData()
s1.printData()
s1.SendData(d1)
d1.drawErrorMsg()
d1.drawSingleDigitError()
d1.distortPacket(s1)
d1.drukuj()
d1.passToReceiver(r1)
r1.drukuj()