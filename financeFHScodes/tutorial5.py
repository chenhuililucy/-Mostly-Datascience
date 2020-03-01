""" 

Want timeseries and cross sectional data 

""" 


        #=================time series===================#


import csv 
import matplotlib.pylab as plt 
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)


countrylist=["australia","united kingdom","austria","united states","italy"]       
 #select 4 random countries, including the UK 


count=0


for i in countrylist: # iterate through country list 

    with open("tutorial5.csv","r",encoding="utf-8", errors="ignore") as csvfile: 

        file1=csv.reader(csvfile)

        dictionary={}

        count+=1

        if count==6: break

        for row in file1: 

            if row[1].lower()==i:

                dictionary.update({int(row[4]):float(row[12])})

        csvfile.close()

        list=sorted(dictionary.items(), key=lambda t: t[1])

        #ax=plt.gca()
        
        x, y= zip(*list)

        fig, ax = plt.subplots(figsize=(10, 8))

        #ax = fig.add_subplot(1, 1, 1)
        ax.set(xlim=(1999,2019))

        # Change major ticks 
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator((max(y)-min(y))/10))

        # Change minor ticks 
        ax.xaxis.set_minor_locator(AutoMinorLocator(0.2))
        ax.yaxis.set_minor_locator(AutoMinorLocator((max(y)-min(y))/50))

        # Turn grid on for both major and minor ticks and style minor slightly
        # differently.
        ax.grid(which='major', color='#CCCCCC', linestyle='--')
        ax.grid(which='minor', color='#CCCCCC', linestyle=':')

        plt.scatter(*zip(*list))


        plt.xlabel("Year")
        plt.ylabel("Debt to equity ratio of non-financial corporations"+":"+i)

        par = np.polyfit(x, y, 1, full=True)


        slope=par[0][0]

        intercept=par[0][1]

        xl = [min(x), max(x)]

        yl = [slope*xx + intercept  for xx in xl]

        variance = np.var(y)

        residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(x,y)])
        Rsqr = np.round(1-residuals/variance, decimals=2)
        plt.text(.9*max(x)+.1*min(x),.9*max(y)+.1*min(y),'$R^2 = %0.2f$'% Rsqr, fontsize=30)

        yerr = [abs(slope*xx + intercept - yy)  for xx,yy in zip(x,y)]
        par = np.polyfit(x, yerr, 2, full=True)

        yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(x,y)]
        yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(x,y)]

        plt.plot(xl, yl, '-r')
        #plt.plot(x, yerrLower, '--r') 
        #plt.plot(x, yerrUpper, '--r')

        plt.show()





"""

print(x)
listx=list(x)
listy=list(y)

Xaxis= np.linspace(min(x), max(x), 100)
Yaxis= np.linspace(min(y), max(y), 100)
plt.scatter(figsize=(1,5))
plt.plot(x,y)
plt.show()

""" 


            




