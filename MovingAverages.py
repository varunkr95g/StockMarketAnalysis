import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close','Volume'])

#Calculation of the rolling Close value of the past 20 days.
short_rolling = df['Close'].rolling(window=20).mean()

df['20DayClosingValue']=short_rolling

#When the close value goes above the simple 20 day moving average it tends to indicate a bullsih pattern.
df['BullsihBreakout']=np.where(df["Close"]>df["20DayClosingValue"],1,0)


rslt_df = df[df['BullsihBreakout']==1]
# print(rslt_df[["Date","Open","Close","20DayClosingValue"]])

#When the close value goes below the simple 20 day moving average it tends to indicate a bearish pattern.


df['BearishBreakout']=np.where(df["Close"]<df["20DayClosingValue"],1,0)

rslt_df_2 = df[df['BearishBreakout']==1]

print(rslt_df_2[["Date","Open","Close","20DayClosingValue"]])

# Other moving averages ( like the 50 day, 100 day) are also used.
