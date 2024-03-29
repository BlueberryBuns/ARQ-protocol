import csv
   
from Dis import Dis
from Receiver import Receiver
from Sender import Sender
with open('wynikiARQCRC.csv', 'w', newline='') as fileCRC:
    fieldnames = ['ilosc pakietow','przeklamane wiadomosci','jedno powtorzenie','dwa powtorzenia','trzy powtorzenia','cztery powtorzenia','piec i wiecej']
    writer = csv.writer(fileCRC)
    writer.writerow(fieldnames)
with open('wynikiARQParity.csv', 'w', newline='') as fileParity:
    fieldnames = ['ilosc pakietow','przeklamane wiadomosci','jedno powtorzenie','dwa powtorzenia','trzy powtorzenia','cztery powtorzenia','piec i wiecej']
    writer = csv.writer(fileParity)
    writer.writerow(fieldnames)
for repetition in range(50):
    s1 = Sender()
    d1 = Dis()
    r1 = Receiver()

    print(f"{repetition}\n")

    counterOne = 0
    counterTwo = 0
    counterThree = 0
    counterFour = 0
    counterFive = 0
    counterOverTwo = 0
    ackErrorBadMsgIsGutMsg = 0
    #ackErrorGutMsgIsBadMsg = 0

    #print(d1.singleDigitErrorProb)

    numberOfPackets = 100000

    s1.keyUpdate(r1)
    for i in range(numberOfPackets):
        j = 0
        s1.data.clear()
        s1.sentData.clear()
        d1.dataSendBySender.clear()
        d1.dataReceivedByReceiver.clear()
        s1.makeData(i)
        s1.updateData()
        s1.encodeCRC()
        #s1.printData()
        while not s1.receivedAck:
            j += 1
            s1.SendData(d1)
            d1.drawErrorMsg()
            d1.drawSingleDigitError()
            d1.distortPacket(s1)
            #d1.drukuj()
            d1.passToReceiver(r1)
            #r1.drukuj()
            r1.decodeCRC(s1)
            if r1.receivedData != s1.sentData and r1.ackMessage:
                ackErrorBadMsgIsGutMsg += 1
            # if r1.receivedData == s1.sentData and r1.ackMessage == False:
            #     ackErrorGutMsgIsBadMsg += 1
            # print(s1.receivedAck)
            #print("TU JEST KONIEC!!!!!!!!!!")
        if j == 1:
            counterOne += 1
        elif j == 2:
            counterTwo += 1
        elif j == 3:
            counterThree += 1
        elif j == 4:
            counterFour += 1
        elif j >= 5:
            counterFive += 1

        s1.receivedAck = False

    #print(numberOfPackets)
    #print(ackErrorBadMsgIsGutMsg)
    #print(counterOne)
    #print(counterTwo)
    #print(counterThree)
    #print(counterFour)
    #print(counterFive)
    resultsCRC = [numberOfPackets,ackErrorBadMsgIsGutMsg,counterOne,counterTwo,counterThree,counterFour,counterFive]

    #print()

    counterOne = 0
    counterTwo = 0
    counterThree = 0
    counterFour = 0
    counterFive = 0
    ackErrorBadMsgIsGutMsg = 0
    #ackErrorGutMsgIsBadMsg = 0



    for i in range(numberOfPackets):
        j = 0
        s1.data.clear()
        s1.sentData.clear()
        d1.dataSendBySender.clear()
        d1.dataReceivedByReceiver.clear()
        s1.makeData(i)
        s1.encodeParity()
        s1.updateData()
        #s1.printData()
        while not s1.receivedAck:
            j += 1
            d1.dataReceivedByReceiver.clear()
            s1.SendData(d1)
            d1.drawErrorMsg()
            d1.drawSingleDigitError()
            d1.distortPacket(s1)
            #d1.drukuj()
            d1.passToReceiver(r1)
            r1.decodeParityData(s1)
            #r1.drukuj()
            if r1.receivedData != s1.data and r1.ackMessage == True:
                ackErrorBadMsgIsGutMsg += 1
            # if r1.receivedData == s1.data and r1.ackMessage == False:
            #     ackErrorGutMsgIsBadMsg += 1
            #print(s1.receivedAck)
        if j == 1:
            counterOne += 1
        elif j == 2:
            counterTwo += 1
        elif j == 3:
            counterThree += 1
        elif j == 4:
            counterFour += 1
        elif j >= 5:
            counterFive += 1

        s1.receivedAck = False

    #print(numberOfPackets)
    #print(ackErrorBadMsgIsGutMsg)
    #print(counterOne)
    #print(counterTwo)
    #print(counterThree)
    #print(counterFour)
    #print(counterFive)
    resultsPARITY = [numberOfPackets,ackErrorBadMsgIsGutMsg,counterOne,counterTwo,counterThree,counterFour,counterFive]
    results = []
    results.append(resultsCRC)
    results.append(resultsPARITY)

    with open('wynikiARQCRC.csv', 'a+', newline='') as fileCRC:
        writer = csv.writer(fileCRC)
        writer.writerow(resultsCRC)
    with open('wynikiARQParity.csv', 'a+', newline='') as fileParity:
        writer = csv.writer(fileParity)
        writer.writerow(resultsPARITY)

    resultsPARITY.clear()
    resultsCRC.clear()
    results.clear()


    # print(f"CRC")
    # print(f"Prawdopodobienstwo zaklamania pojedynczego bitu w pakiecie: {d1.singleDigitErrorProb}%")
    # print(f"Pakiety, ktore potrzebowaly jednego wyslania: {counterOne}")
    # print(f"Pakiety, ktore potrzebowaly dwoch wyslan: {counterTwo}")
    # print(f"Pakiety, ktore potrzebowaly wiecej niz dwoch wyslan: {counterOverTwo}")
    # print(f"Pakiety, ktore zostaly uznane za dobre a byly zle: {ackErrorBadMsgIsGutMsg}")
    # print(f"Pakiety, ktore zostaly uznane za zle a byly dobre: {ackErrorGutMsgIsBadMsg}")
    # #print(countermax)
    # print(f"PARITY")
    # print(f"Prawdopodobienstwo zaklamania pojedynczego bitu w pakiecie: {d1.singleDigitErrorProb}%")
    # print(f"Pakiety, ktore potrzebowaly jednego wyslania: {counterOne}")
    # print(f"Pakiety, ktore potrzebowaly dwoch wyslan: {counterTwo}")
    # print(f"Pakiety, ktore potrzebowaly wiecej niz dwoch wyslan: {counterOverTwo}")
    # print(f"Pakiety, ktore zostaly uznane za dobre a byly zle: {ackErrorBadMsgIsGutMsg}")
    # print(f"Pakiety, ktore zostaly uznane za zle a byly dobre: {ackErrorGutMsgIsBadMsg}")
    # '''
    # ile pakietow potrzebowalo jednego wyslania
    # ile dwoch i ile 3 i więcej
