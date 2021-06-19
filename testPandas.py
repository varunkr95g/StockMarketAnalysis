import pandas as pd

data=[['17/03/21',42.700001,43.400002,40.549999,41.000000,0],
['18/03/21',41.599998,42.450001,40.150002,41.400002,0],
['19/03/21',40.849998,42.450001,39.099998,41.000000,0],
['22/03/21',41.349998,42.900002,40.950001,41.849998,0],
['23/03/21',42.000000,43.700001,42.000000,42.700001,0],
['24/03/21',42.349998,43.150002,41.200001,41.650002,0],
['25/03/21',41.700001,41.750000,39.799999,40.549999,0],
['26/03/21',41.000000,41.299999,40.049999,40.849998,1]]

df = pd.DataFrame(data, columns = ['Date', 'Open','High','Low','Close','PaperHammer'])

# print(df)

closed_values=[]

for i in range(6):
    closed_values.append(df.loc[df['PaperHammer'].shift(-i) == 1, 'Close'].item())

print(closed_values)

if(closed_values==sorted(closed_values,reverse=True)):
    print(1)
else:
    print("No Trend")

# print(df.loc[df['PaperHammer'].shift(-1) == 1, 'Close'].item())
