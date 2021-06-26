import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

#Piercing pattern is a multiple candlestick pattern. It's formed when on Day 1 there's a downtrend
# and on Day 2 there's an upward trend and the Close of Day 2 > Open of Day 1. The body of Day 2 should
# be atleast 50% body of Day 1. Also, I have put the criteria of at least a percent difference between
# Open and Close on Day 1 to prevent Dojis from being considered.

df['PiercingPattern']=np.where((df.Open.shift(1)>df.Close.shift(1)) & (df["Close"]>df.Open.shift(1))
                                       & ((df["Close"]-df["Open"])>0.5*(df.Open.shift(1) - df.Close.shift(1)))
                                       & ((df.Open.shift(1) - df.Close.shift(1))/df.Open.shift(1)>0.01),1,0)

rslt_df = df[df['PiercingPattern']==1]

print(rslt_df[["Date","Open","Close","PiercingPattern"]])

bearish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(1,5):
        closed_values.append(df.loc[df['PiercingPattern'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values)):
        bearish_pattern_exists.append("Yes")

    else:
        bearish_pattern_exists.append("No")

print(bearish_pattern_exists)

for i in bearish_pattern_exists:
    if(i=="Yes"):
        print("Piercing Pattern formed")
    else:
        print("No accurate trend")
