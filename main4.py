import pandas as pd
import numpy as np

info = {'Id':[1,2,3,4],
        'Name':['Pankaj','Meghna','David','Lisa'],
        'Role':['CEO',np.nan,np.nan,np.nan],
        'Salary':[100,200,np.nan,np.nan]}

labels = ['a','b','c','d']

df = pd.DataFrame(info , index = labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())