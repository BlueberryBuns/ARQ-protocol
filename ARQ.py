import random
#sam komentarzy nie robisz pajacu
msg = []
initialmessages = []
disturbedmessages = []
distortedzerotoone= 0
distortedonetozero = 0
distortedunchanged = 0
msgsize = int(input("Podaj ilosc bitow do wyslania: "))
packetsize = int(input("Podaj wielkosc pojedynczego pakietu: "))
errorprob = float(input("Podaj prawdopodobienstwo wystapienia zaklocenia bitu wyrazone w % : "))
packetnumer = int(0)
numberofmessages = int(input("Podaj ilosc wiadomosci do wyslania: "))
for j in range(numberofmessages):
    for i in range(msgsize):
        rand = random.randint(0, 1)
        msg.append(rand)

    initialmessages.append(msg)
    print(f"Wiadomosc przed zakloceniem: {initialmessages[j]}")

    disturbedmsg = list(msg)
    for i in range(msgsize):
        rand = random.randint(0, 100)
        if errorprob >= rand:
            distortion = random.randint(0,1)
            if disturbedmsg[i] == distortion:
                distortedunchanged += 1
                disturbedmsg[i] = distortion
            elif distortion == 1 and disturbedmsg[i] == 0:
                distortedzerotoone+= 1
                disturbedmsg[i] = distortion
            elif distortion == 0 and disturbedmsg[i] == 1:
                distortedonetozero+= 1
                disturbedmsg[i] = distortion
            else:
                print("Cos niedobrego sie stalo")

    disturbedmessages.append(disturbedmsg)
    print(f"Wiadomosc po zakloceniu    : {disturbedmsg}")

    packetsbefore = []
    packetsafter = []
    while ((packetnumer + 1) * packetsize) - 1 <= msgsize - 1:
        packetsbefore.append(msg[packetnumer * packetsize:  ((packetnumer + 1) * packetsize)])
        print(f"Pakiet nr {packetnumer + 1} : {packetsbefore[packetnumer]} przed zakloceniem")
        packetsafter.append(disturbedmsg[packetnumer * packetsize:  ((packetnumer + 1) * packetsize)])
        print(f"Pakiet nr {packetnumer + 1} : {packetsafter[packetnumer]} po zakloceniu")
        packetnumer += 1
# abc
