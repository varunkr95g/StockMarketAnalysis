import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

#Bearish Engulfing pattern with Doji is a multiple candlestick pattern. It's formed when on Day 1 there's a uptrend
# and on Day 2 there's an downward trend and the Close of Day 2 < Open of Day 1. The body of Day 2 should also
# be greater than body of Day 1. Also, I have put the criteria of at least a percent difference between
# Open and Close on Day 1 to prevent Dojis from being considered. Day 3 should be a Doji.

df['BearishEngulfingPatternWithDoji']=np.where((df.Open.shift(2)<df.Close.shift(2)) & (df.Close.shift(1)<df.Open.shift(2))
                                       & (abs(df.Open.shift(1)-df.Close.shift(1))>abs(df.Close.shift(2) - df.Open.shift(2)))
                                       & ((df.Close.shift(2) - df.Open.shift(2))/df.Open.shift(2)>0.01)
                                       & (abs(df["Close"]-df["Open"])<=0.015) & ((df["High"]-df["Close"])/df["Close"] >=0.01)

                                       &  ((df["Open"]-df["Low"])/df["Open"] >=0.01) & (df["Date"]>'04/01/21'),1,0)

rslt_df = df[df['BearishEngulfingPatternWithDoji']==1]

print(rslt_df[["Date","Open","Close","BearishEngulfingPatternWithDoji"]])

# Check for prior Bullish pattern
prior_bullish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(2,7):
        closed_values.append(df.loc[df['BearishEngulfingPatternWithDoji'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values,reverse=True)):
        prior_bullish_pattern_exists.append("Yes")

    else:
        prior_bullish_pattern_exists.append("No")

print(prior_bullish_pattern_exists)

for i in prior_bullish_pattern_exists:
    if(i=="Yes"):
        print("BearishEngulfing Pattern With Doji formed")
    else:
        print("No accurate trend")
