import pandas as pd
from sklearn import preprocessing

FILE_PATH = "./Data/numerical.csv"
DEST_PATH = './Data/numerical_2.csv' 
df = pd.read_csv(FILE_PATH, encoding='utf-8', error_bad_lines=False)
# Elimina renglones con algún valor NULL #
df = df.dropna()
# Reset a los valores del index en el dataframe #
df = df.reset_index(drop=True)
df = df.replace(to_replace='Li-ion', value='Li-Ion')


df.to_csv(DEST_PATH, index=False)