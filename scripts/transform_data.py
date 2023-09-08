import pandas as pd

#Reading file in data folder using pandas
df = pd.read_csv('../data/penguins.csv',sep=',')

print(df.groupby('sex')['island'].size().reset_index())
