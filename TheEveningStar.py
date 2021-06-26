import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

# The Evening Star pattern is formed when there's a Green Candle on day 1, gap up opening on Day 2 and a doji, gap down opening on Day 3
# The close on Day 3 should be lower than the Open of Day 1
df['TheEveningStar']=np.where( (df.Close.shift(2)>df.Open.shift(2))
                                & (df.Open.shift(1)>df.Close.shift(2)) & (df["Open"] < df.Close.shift(1)) & (df["Close"] < df.Open.shift(2))
                               &(df["Open"]>df["Close"]) & ((abs(df.Close.shift(1)-df.Open.shift(1))/df.Open.shift(1))<=0.015)
                                ,1,0)





rslt_df = df[df['TheEveningStar']==1]

print(rslt_df[["Date","Open","Close","TheEveningStar"]])

#Since No valid values exist for the above criteria, we will not check for the prior bullsih trend.

# bearish_pattern_exists=[]
#
# for i in range(len(rslt_df)):
#     closed_values = []
#     for j in range(2,7):
#         closed_values.append(df.loc[df['TheMorningStar'].shift(-j) == 1, 'Open'].iloc[i])
#
#     # print(closed_values)
#     if (closed_values == sorted(closed_values)):
#         bearish_pattern_exists.append("Yes")
#
#     else:
#         bearish_pattern_exists.append("No")
#
# print(bearish_pattern_exists)
#
# for i in bearish_pattern_exists:
#     if(i=="Yes"):
#         print("TheMorningStar Pattern formed")
#     else:
#         print("No accurate trend")
