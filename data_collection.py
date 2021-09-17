import MAROCANNONCESscraping as ma
import REKRUTscraping as rs
import EMPLOIMAscraping as em

import pandas as pd

df1 =ma.df
df2=rs.df
df3=em.df
df4 = pd.concat([df1, df2, df3])

df4.to_csv('./csvFiles/data_collection.csv', index = False)