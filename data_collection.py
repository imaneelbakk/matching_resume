import MAROCANNONCESscraping as ma
import REKRUTscraping as rs

import pandas as pd



df1 =ma.df
df2=rs.df
df3 = pd.concat([df1, df2])

df3.to_csv('./csvFiles/data_collection.csv', index = False)
