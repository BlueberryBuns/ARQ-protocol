import random

msg = []
msgsize = int(input("Podaj ilosc bitow do wyslania: "))
packetsize = int(input("Podaj wielkosc pojedynczego pakietu: "))
errorprob = int(input("Podaj prawdopodobienstwo wystapienia zaklocenia bitu wyrazone w % : "))
packetnumer = int(0)

for i in range(msgsize):
    rand = random.randint(0, 1)
    msg.append(rand)

print(f"Wiadomosc przed zakloceniem: {msg}")
disturbedmsg = msg

for i in range(msgsize):
    rand = random.randint(0, 100)
    if errorprob >= rand:
        if disturbedmsg[i] == 0:
            disturbedmsg[i] = 1
        else:
            disturbedmsg[i] = 0

print(f"Wiadomosc po zakloceniu    : {disturbedmsg}")


while ((packetnumer + 1) * packetsize) - 1 <= msgsize - 1:
    packet = [disturbedmsg[packetnumer * packetsize:  ((packetnumer + 1) * packetsize)]]
    print(f"Pakiet nr {packetnumer+1} : {packet}")
    packetnumer += 1

