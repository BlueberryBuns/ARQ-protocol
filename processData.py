#import pdb; pdb.set_trace  ()
import pandas as pd
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec as gs

#import csv

def f(x,mean,amplitude,std_deviation):
    return amplitude*numpy.exp(-((x-mean)/std_deviation)**2)

n_points = 800
#n_bins = int(1 + numpy.floor(3.3*numpy.log(n_points)))
n_bins = 20
for number in range(1,9):
    dfCRC = pd.read_csv(f'wynikiARQ{number}Parity.csv')
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

    #print(data_frame)
    for k in list_of_cont:

    
        fig = plt.figure()
        grid = gs(5,1,figure = fig)
        
        ax1 = fig.add_subplot(grid[0,0])
        ax2 = fig.add_subplot(grid[1:,0])
        #ax1.axis('off')
        ax1.axes.get_xaxis().set_visible(False)
        #ax1.axes.get_yaxis().set_visible(False)
        ax2.grid()
        ax1.boxplot(k[k!=0], vert = False)
        x, y, z = ax2.hist(k[k!=0], bins =  n_bins)
        bins_center = y[:-1]+numpy.diff(y)/2
        #ax1.get_shared_x_axes().join(ax1,ax2)
        if k.name == 'jedno powtorzenie': param_index = 1
        elif k.name == 'przeklamane wiadomosci': param_index = 0
        elif k.name == 'dwa powtorzenia': param_index = 2
        elif k.name == 'trzy powtorzenia': param_index = 3
        elif k.name == 'cztery powtorzenia': param_index = 4
        elif k.name == 'piec i wiecej': param_index = 5
        
        params, matrix= curve_fit(f, bins_center, x, p0=[meanList[param_index], 0, st_div[param_index]], maxfev=50000)
        ax1.grid()
        type_of_coding = 'Parity'
        if k.name == 'jedno powtorzenie': tmpname = f'Pomyślnie wysłane za pierwszym razem {number} {type_of_coding}'
        elif k.name == 'przeklamane wiadomosci': tmpname = f'Przyjęte wiadomości przekłamane {number} {type_of_coding}'
        elif k.name == 'dwa powtorzenia': tmpname = f'Pomyślnie wysłane przy drugiej próbie {number} {type_of_coding}'
        elif k.name == 'trzy powtorzenia': tmpname = f'Pomyślnie wysłane przy trzeciej próbie {number} {type_of_coding}'
        elif k.name == 'cztery powtorzenia': tmpname = f'Pomyślnie wysłane przy czwartej próbie {number} {type_of_coding}'
        elif k.name == 'piec i wiecej': tmpname = f'Pomyślnie wysłane przy piątej lub większej ilości prób {number} {type_of_coding}'
        fig.suptitle(tmpname)
        
        ax2.plot(bins_center,f(bins_center,*params))
        ax2.set_xlabel("liczba pakietów")
        ax2.set_ylabel("liczba wystąpień")
        plt.show()