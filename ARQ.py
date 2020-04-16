import random
list = []
msgsize = int(input("Podaj ilosc bitow do wyslania: "))
packetsize = int(input("Podaj wielkosc pojedynczego pakietu: "))
packetnumer = int(0)
for i in range(msgsize):
    y = random.randint(0,1)
    list.append(y)

print(list)

while ((packetnumer+1)*packetsize)-1 <= msgsize-1:
    print(list[packetnumer*packetsize :  ((packetnumer+1)*packetsize)])
    packetnumer += 1 #123