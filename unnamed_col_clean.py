import pandas as pd
import numpy as np
df = pd.read_csv('label_file.csv', na_values='NaN', keep_default_na=False)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
print(np.count_nonzero(df.isnull().values))
print(df.head())
df.to_csv('label_file_final.csv')
