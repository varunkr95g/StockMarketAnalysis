import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

# ShootingStar pattern exists when the body of the candlestick is atmost half of the upper shadow of the candlestick.
# Also, the body needs to be relatively small. The low formed should also be relatively small.
# The below logic takes care of that.

df['ShootingStar']=np.where( ( (abs(df["Close"]-df["Open"]))/df["Open"] <=0.015) &
                            (abs(df[["Close","Open"]].min(axis=1)-df["High"])>=2*(abs(df["Close"]-df["Open"])))
                            & (  (abs(df[["Close","Open"]].max(axis=1)-df["Low"]))/(df[["Close","Open"]].max(axis=1))<=0.01)

                            ,1,0)

rslt_df = df[df['ShootingStar']==1]

# print(rslt_df[["Date","ShootingStar"]])

# Shooting Star is useful only when it's preceded by a bullish pattern. If no such pattern exists, a Shooting Star pattern isn't formed.
#Below logic takes care of identifying a bullish pattern.

bullish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(6):
        closed_values.append(df.loc[df['ShootingStar'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values)):
        bullish_pattern_exists.append("Yes")

    else:
        bullish_pattern_exists.append("No")

# print(bearish_pattern_exists)

for i in bullish_pattern_exists:
    if(i=="Yes"):
        print("ShootingStar Pattern formed")
    else:
        print("No accurate trend")
