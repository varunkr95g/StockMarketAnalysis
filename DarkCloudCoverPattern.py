import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

#Dark Cloud Cover pattern is a multiple candlestick pattern. It's formed when on Day 1 there's a uptrend
# and on Day 2 there's an downward trend . The body of Day 2 should also
# be atleast 50% of body of Day 1. Also, I have put the criteria of at least a percent difference between
# Open and Close on Day 1 to prevent Dojis from being considered.

df['DarkCloudCoverPattern']=np.where((df.Open.shift(1)<df.Close.shift(1)) &(df["Open"]>df["Close"])
                                       & (abs(df["Open"]-df["Close"])>0.5*(abs(df.Close.shift(1) - df.Open.shift(1))))
                                       & ((df.Close.shift(1) - df.Open.shift(1))/df.Open.shift(1)>0.01) & (df["Date"]>'04/01/21'),1,0)

rslt_df = df[df['DarkCloudCoverPattern']==1]

print(rslt_df[["Date","Open","Close","DarkCloudCoverPattern"]])

# Check for prior Bullish pattern
prior_bullish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(1,6):
        closed_values.append(df.loc[df['DarkCloudCoverPattern'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values,reverse=True)):
        prior_bullish_pattern_exists.append("Yes")

    else:
        prior_bullish_pattern_exists.append("No")

print(prior_bullish_pattern_exists)

for i in prior_bullish_pattern_exists:
    if(i=="Yes"):
        print("BearishEngulfing Pattern formed")
    else:
        print("No accurate trend")
