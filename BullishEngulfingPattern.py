import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

df['BullsihEngulfingPattern']=np.where((df.Open.shift(1)>df.Close.shift(1)) & (df["Close"]>df.Open.shift(1))
                                       & ((df["Close"]-df["Open"])>(df.Open.shift(1) - df.Close.shift(1)))
                                       & ((df.Open.shift(1) - df.Close.shift(1))/df.Open.shift(1)>0.01),1,0)

rslt_df = df[df['BullsihEngulfingPattern']==1]

print(rslt_df[["Date","Open","Close","BullsihEngulfingPattern"]])

bearish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(1,7):
        closed_values.append(df.loc[df['BullsihEngulfingPattern'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values)):
        bearish_pattern_exists.append("Yes")

    else:
        bearish_pattern_exists.append("No")

print(bearish_pattern_exists)

for i in bearish_pattern_exists:
    if(i=="Yes"):
        print("BullsihEngulfing Pattern formed")
    else:
        print("No accurate trend")
