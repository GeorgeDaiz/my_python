import pandas as pd
import numpy as np

df = pd.read_csv('data/Diamonds.csv')
# print(df.head())
# a1
# a = df.groupby(df['carat'] > 1)['price'].apply(lambda x: x.max() - x.min())
# a2
# df_r = df.query('carat > 1')['price']
# a = df_r.max() - df_r.min()
# print(a)

# bins = df['depth'].quantile(np.linspace(0, 1, 6)).tolist()
# cuts = pd.cut(df['depth'], bins=bins)
# b = df.groupby(cuts)['color'].apply(lambda x: x.value_counts().nlargest(1))
# print(b)



