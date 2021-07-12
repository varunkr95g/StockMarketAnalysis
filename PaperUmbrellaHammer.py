import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.read_csv("data_Sanghi.csv",usecols=['Date','Open','High','Low','Close'])

# Paper Hammer pattern exists when the body of the candlestick is atmost half of the lower shadow of the candlestick.
# Also, the body needs to be relatively small. The high formed should also be relatively small.
# The below logic takes care of that.

df['PaperHammer']=np.where( ( (abs(df["Close"]-df["Open"]))/df["Open"] <=0.015) &
                            (abs(df[["Close","Open"]].min(axis=1)-df["Low"])>=2*(abs(df["Close"]-df["Open"])))
                            & (  (abs(df[["Close","Open"]].max(axis=1)-df["High"]))/(df[["Close","Open"]].max(axis=1))<=0.01)

                            ,1,0)



rslt_df = df[df['PaperHammer']==1]

# print(rslt_df[["Date","PaperHammer","Open","Low","High","Close"]])


# Paper Hammer is useful only when it's preceded by a bearish pattern. If no such pattern exists, a paper hammer isn't formed.
#Below logic takes care of identifying a bearish pattern.
bearish_pattern_exists=[]

for i in range(len(rslt_df)):
    closed_values = []
    for j in range(6):
        closed_values.append(df.loc[df['PaperHammer'].shift(-j) == 1, 'Open'].iloc[i])

    # print(closed_values)
    if (closed_values == sorted(closed_values, reverse=True)):
        bearish_pattern_exists.append("Yes")

    else:
        bearish_pattern_exists.append("No")

# print(bearish_pattern_exists)

for i in bearish_pattern_exists:
    if(i=="Yes"):
        print("Hammer Pattern formed")
    else:
        print("No accurate trend")











