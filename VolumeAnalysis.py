import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close','Volume'])


#Calculation of the rolling volume of the past 10 days.
short_rolling = df['Volume'].rolling(window=10).mean()


df['AvergaeVolume']=short_rolling


# Bullish Volume breakout happens when the stock price goes up and the volume is greater than the 10 day volume.
df['BullishVolumeBreakout']=np.where((df["Volume"]>df['AvergaeVolume']) &
                                     ((df["Close"]-df["Open"])/df["Open"]>=0.02)
                                     ,1,0)

rslt_df = df[df['BullishVolumeBreakout']==1]

# print(rslt_df[["Date","Open","Close","Volume","AvergaeVolume"]])


# Bearish Volume breakout happens when the stock price goes down and the volume is greater than the 10 day volume.
df['BearishVolumeBreakout']=np.where((df["Volume"]>df['AvergaeVolume']) &
                                     ((df["Open"]-df["Close"])/df["Open"]>=0.02)
                                     ,1,0)

rslt_df_2 = df[df['BearishVolumeBreakout']==1]

print(rslt_df_2[["Date","Open","Close","Volume","AvergaeVolume"]])



