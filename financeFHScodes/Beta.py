# coding: utf-8


# In[79]:

import os

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime


from pandas_datareader import data as pdr
import yfinance as yf


"""
#Guide to use Yahoo finance 

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
stock.major_holders

# show institutional holders
stock.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts

""" 


#scraping the data from Yahoo! finance and returning a Pandas DataFrame

yf.pdr_override() #overriding 


startD="2010-01-01"
endD="2020-01-01"
stocks=["GOOG", "SPY"]

df1 = pdr.get_data_yahoo("GOOG", start=startD, end=endD)
#print(df1.head())

df2 = pdr.get_data_yahoo("SPY", start=startD, end=endD)
#print(df1.head())

start_date = pd.to_datetime(startD) 
end_date = pd.to_datetime(endD)


"""

Modified to download monthly data 
https://stackoverflow.com/questions/52463555/how-to-download-monthly-frequency-stock-closing-price-from-yahoo-finance-using-p

"""

n = 1  

#return Google data frame
mon_data1=pd.DataFrame(df1['Adj Close'].resample('BM').apply(lambda x: x[-1-n])) 
#print(mon_data1)

#return SPY data frame
mon_data2=pd.DataFrame(df1['Adj Close'].resample('BM').apply(lambda x: x[-1-n])) 

end_of_months1 = mon_data1.index.tolist()
end_of_months1[-1] = df1.index[-1]
mon_data1.index = end_of_months1


end_of_months2 = mon_data2.index.tolist()
end_of_months2[-1] = df2.index[-1]
mon_data2.index = end_of_months2


mon_data1.index = mon_data1.index - datetime.timedelta(days=n)
mon_data2.index = mon_data2.index - datetime.timedelta(days=n)

def download_data(stocks):
    data = pdr.get_data_yahoo(stocks, start=start_date, end=end_date)['Adj Close']  
    #print(data)
    return data

download_data(stocks)

# In[80]:


# We have to take the percent changes to get to returns hence we will use .pct_change()
# We do not want the first (0th) element because it is NAN


return_goog = df1.Close.pct_change()[1:]
return_spy = df2.Close.pct_change()[1:]


# We will plot the returns of Google and S&P500 against each other
plt.figure(figsize=(20,10))
return_goog.plot()
return_spy.plot()
plt.ylabel("Daily Return of GOOG and SPY")
plt.show()

return_googmon = mon_data1.pct_change(axis="rows")[1:]
print(return_googmon)
return_spymon = mon_data2.pct_change(axis="rows")[1:]
print(return_spymon)

plt.figure(figsize=(20,10))
return_googmon.plot()
return_spymon.plot()
plt.ylabel("Monthly Return of GOOG and SPY")
plt.show()

# In[81]:


import statsmodels.api as sm
from statsmodels import regression


X = return_spy.values
Y = return_goog.values
A = return_googmon.values
B = return_spymon.values

def linreg(x,y):



    x = sm.add_constant(x) #An intercept is not included by default 

    model = regression.linear_model.OLS(y,x).fit()
 
    # We are removing the constant 
    """ 
    sample usage: 
    
    Out[37]: 
    array([[ 0.03196827,  0.50048646],
       [ 0.85928802,  0.50081615],
       [ 0.11140678,  0.88828011]])

    x = x[:,1]

    x
    Out[39]: array([ 0.50048646,  0.50081615,  0.88828011])

    """ 

    x = x[:, 1]
    return model.params[0], model.params[1]


alpha, beta = linreg(X,Y)
alphamon, betamon = linreg(A,B)

print('alpha: ' + str(alpha))
print('beta: ' + str(beta))

print('alpha:(mon)' + str(alphamon))
print('beta:(mon) ' + str(betamon))


# In[82]:


X2 = np.linspace(X.min(), X.max(), 100) #Returns number spaces evenly w.r.t interval.
Y_hat = X2 * beta + alpha


plt.figure(figsize=(10,7))
plt.scatter(X, Y, alpha=0.3) # Plot the raw data
plt.xlabel("SPY Daily Return")
plt.ylabel("GOOG Daily Return")


plt.plot(X2, Y_hat, 'r', alpha=0.9)


plt.show()

X2 = np.linspace(A.min(), B.max(), 100) #Returns number spaces evenly w.r.t interval.
Y_hat = X2 * betamon + alphamon


plt.figure(figsize=(10,7))
plt.scatter(A, B, alpha=0.3) # Plot the raw data
plt.xlabel("SPY Monthly Return")
plt.ylabel("GOOG Monthly Return")


plt.plot(X2, Y_hat, 'r', alpha=0.9)


plt.show()

