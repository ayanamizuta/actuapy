import pandas as pd
import numpy as np

def is_same_df(df1,df2,name_check=False):
    #print(df1.columns.values,df2.columns.values)
    #print(df1.index.values,df2.index.values)
    #print(df1)
    #print(df2)
    if name_check:
        assert np.array_equal(df1.columns.values,df2.columns.values), "not same columns"
        assert np.array_equal(df1.index.values  ,df2.index.values),   "not same index"
    return np.linalg.norm(df1.values-df2.values) < 0.0001
