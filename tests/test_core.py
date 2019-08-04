import unittest
import pandas as pd
import os,sys
from actuapy.util import *

test_data_path = os.path.abspath(os.path.dirname(__file__))+"/data/"

class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
        pass

    def test_predict_lifetable(self):
        from actuapy.core import LifeTable
        df = pd.read_csv(test_data_path+"core_lifetable.csv",dtype={0:str})
        df.set_index('Unnamed: 0',inplace=True)
        lt = LifeTable(df,datatype="lifetable")
        assert is_same_df(lt.lifetable.l,df),"lifetable.l"
        df=pd.read_csv(test_data_path+"core_lifetable_d.csv",dtype={0:str})
        df.set_index('Unnamed: 0',inplace=True)
        assert is_same_df(lt.lifetable.d,df),"lifetable.d"
        df = pd.read_csv(test_data_path+"core_lifetable_quit_rate.csv",dtype={0:str})
        df.set_index('Unnamed: 0',inplace=True)
        assert is_same_df(lt.quit_rate,df),"quit_rate"

    def test_predict_entry(self):
        from actuapy.core import LifeTable
        df = pd.read_csv(test_data_path+"core_entry.csv")
        lt = LifeTable(df,datatype="entry",userid_col='id',time_col='year',age_col='age')
        df = pd.read_csv(test_data_path+"core_entry_l.csv")
        df.set_index('Unnamed: 0',inplace=True)
        assert is_same_df(lt.lifetable.l,df),"lifetable.l"
        df = pd.read_csv(test_data_path+"core_entry_d.csv")
        df.set_index('Unnamed: 0',inplace=True)
        assert is_same_df(lt.lifetable.d,df),"lifetable.d"
        df = pd.read_csv(test_data_path+"core_entry_quit_rate.csv")
        df.set_index('Unnamed: 0',inplace=True)
        assert is_same_df(lt.quit_rate,df),"quit_rate"


if __name__ == '__main__':
    unittest.main()
