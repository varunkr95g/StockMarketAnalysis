import yfinance as yf
import pandas as pd
from nsedata import Nse


df=pd.read_html("https://in.finance.yahoo.com/quote/%5ENSEI/components?p=%5ENSEI")[0]

# print(df)

tickers=df.Symbol.to_list()

tickers_2=[]

for i in tickers:
    if(i!='MM.NS'):
        tickers_2.append(i)

# print(type(tickers_2))
#
# print(tickers_2)

data=yf.download(tickers_2,"2020-01-01")

# print(data)

data.to_csv('/Users/z0027vp/Documents/Test/data.csv')

# print(df.Symbol.to_list())


