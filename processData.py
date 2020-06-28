#import pdb; pdb.set_trace()
import pandas as pd
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec as gs
#import csv

def f_model(x,mean,amplitude,std_deviation):
    return amplitude*numpy.exp(-((x-mean)/std_deviation)**2)

n_points = 800
n_bins = int(1 + numpy.floor(3.3*numpy.log(n_points)))

for number in range(1,9):
    pass
number = 7
dfCRC = pd.read_csv(f'wynikiARQ{number}CRC.csv')
data_frame = pd.DataFrame(dfCRC)
przeklamaneWiadmosci = dfCRC['przeklamane wiadomosci']
jeden = dfCRC['jedno powtorzenie']
dwa = dfCRC['dwa powtorzenia']
trzy = dfCRC['trzy powtorzenia']
cztery = dfCRC['cztery powtorzenia']
pieciwiecej = dfCRC['piec i wiecej']
list_of_cont = []
list_of_cont.append(przeklamaneWiadmosci)
list_of_cont.append(jeden)
list_of_cont.append(dwa)
list_of_cont.append(trzy)
list_of_cont.append(cztery)
list_of_cont.append(pieciwiecej)

meanList = []
meanList.append(przeklamaneWiadmosci.mean())
meanList.append(jeden.mean())
meanList.append(dwa.mean())
meanList.append(trzy.mean())
meanList.append(cztery.mean())
meanList.append(pieciwiecej.mean())

st_div = []
st_div.append(przeklamaneWiadmosci.std())
st_div.append(jeden.std())
st_div.append(dwa.std())
st_div.append(trzy.std())
st_div.append(cztery.std())
st_div.append(pieciwiecej.std())

#print(f'Odchylenie standardowe: {st_div}')

przeklamaneQ = []
przeklamaneQ.append(przeklamaneWiadmosci.quantile(.0))
przeklamaneQ.append(przeklamaneWiadmosci.quantile(.25))
przeklamaneQ.append(przeklamaneWiadmosci.quantile(.5))
przeklamaneQ.append(przeklamaneWiadmosci.quantile(.75))
przeklamaneQ.append(przeklamaneWiadmosci.quantile(1))

jedenQ = []
jedenQ.append(jeden.quantile(.0))
jedenQ.append(jeden.quantile(.25))
jedenQ.append(jeden.quantile(.5))
jedenQ.append(jeden.quantile(.75))
jedenQ.append(jeden.quantile(1))
dwaQ = []
dwaQ.append(dwa.quantile(.0))
dwaQ.append(dwa.quantile(.25))
dwaQ.append(dwa.quantile(.5))
dwaQ.append(dwa.quantile(.75))
dwaQ.append(dwa.quantile(1))
trzyQ = []
trzyQ.append(trzy.quantile(.0))
trzyQ.append(trzy.quantile(.25))
trzyQ.append(trzy.quantile(.5))
trzyQ.append(trzy.quantile(.75))
trzyQ.append(trzy.quantile(1))
czteryQ = []
czteryQ.append(cztery.quantile(.0))
czteryQ.append(cztery.quantile(.25))
czteryQ.append(cztery.quantile(.5))
czteryQ.append(cztery.quantile(.75))
czteryQ.append(cztery.quantile(1))
piecQ = []
piecQ.append(pieciwiecej.quantile(.0))
piecQ.append(pieciwiecej.quantile(.25))
piecQ.append(pieciwiecej.quantile(.5))
piecQ.append(pieciwiecej.quantile(.75))
piecQ.append(pieciwiecej.quantile(1))
print(przeklamaneQ)
print(jedenQ)
print(dwaQ)
print(trzyQ)
print(czteryQ)
print(piecQ)
IQRjeden = jedenQ[3] - jedenQ[1]
IQRdwa = dwaQ[3] - dwaQ[1]
IQRtrzy = trzyQ[3] -trzyQ[1]
IQRcztery = czteryQ[3] - czteryQ[1]
IQRpiec = piecQ[3] - piecQ[1]
IQRprzeklamane = przeklamaneQ[3] - przeklamaneQ[1]
#print(st_div)
print(IQRprzeklamane)
print(IQRjeden)
print(IQRdwa)
print(IQRtrzy)
print(IQRcztery)
print(IQRpiec)
print(data_frame)

fig = plt.figure()
grid = gs(5,1,figure = fig)

ax1 = fig.add_subplot(grid[0,0])
ax2 = fig.add_subplot(grid[1:,0])
#ax1.axis('off')
ax1.axes.get_xaxis().set_visible(False)
#ax1.axes.get_yaxis().set_visible(False)



ax2.grid()

ax1.boxplot(jeden, vert = False)
x, y, z = ax2.hist(jeden, bins =  n_bins)
bins_center = y[:-1]+numpy.diff(y)/2
#ax1.get_shared_x_axes().join(ax1,ax2)
print(bins_center)
xlist = list(x)
ylist = list(y)
print(f"{xlist}\n\n")
print(ylist)

curve_fit(f_model, ylist, xlist)
#print(params)
ax1.grid()
plt.show()
#boxplot = dfCRC.boxplot(column=['jedno powtorzenie','dwa powtorzenia','trzy powtorzenia','cztery powtorzenia','piec i wiecej'])