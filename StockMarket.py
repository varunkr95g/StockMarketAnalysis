import yfinance as yf
import pandas as pd
from nsedata import Nse

#Import the data from Yahoo Finance
df=pd.read_html("https://in.finance.yahoo.com/quote/SANGHIIND.NS?p=SANGHIIND.NS")[0]
data=yf.download("SANGHIIND.NS","2021-01-01")
data.to_csv('data_Sanghi.csv')

# print(df.Symbol.to_list())


