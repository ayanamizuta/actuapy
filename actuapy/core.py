# -*- coding:utf-8 -*-

"""
このモジュールでは、統計的な解析に必要なデータ構造を作るためのクラスを用意します。
"""

__author__ = "Rei Mizuta <ayanamizuta832@gmail.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "28 July 2019"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os,sys
from .helper import *

class LifeTable:
    "生命表または取引のデータから脱退率の計算をします"
    def __init__(self,df=None,\
                 datatype="entry",\
                 userid_col="",\
                 time_col="",\
                 age_vol="",\
                 time_seq=[],\
                 age_seq=[],
                 varbose=False):
        """
        3種類の入力データに対して脱退表を作成します。

        1. 年齢と年度（time_colカラム）をそれぞれ行、列にもつ人数データ (datatype=lifetable を指定)
        2. 人に対してid（userid_colカラム）が振られている申込データ (datatype=entry を指定)
        3.(optional) 年齢と年度（time_colカラム）をそれぞれ行、列にもつ外部の人数データ
        """

        # validation of input
        if datatype == "entry":
            assert userid_col != "", assert_initialize(self,"userid_col","userid_col=id")
            assert time_col   != "", assert_initialize(self,"time_col","time_col=year")
            assert age_col    != "", assert_initialize(self,"age_col","age_col=age")
            
            if len(time_seq) == 0:
                print(assert_initialize(self,"time_seq","time_seq=['2017','2018','2019']"),file=sys.stderr)
                self.time_seq = sort(df[self.time_col].unique())
            else:
                self.time_seq = time_seq
                if set(self.time_seq) != set(df[self.time_col].unique()):
                    print("There is a time value which does not appear in given time_seq",file=sys.stderr)
            assert len(self.time_seq) > 1,"There is at most one time value"

            if len(age_seq) == 0:
                print(assert_initialize(self,"age_seq","age_seq=['20','21','22']"),file=sys.stderr)
                self.age_seq = sort(df[self.age_col].unique())
            else:
                self.age_seq = age_seq
                if set(self.age_seq) != set(df[self.age_col].unique()):
                    print("There is a age value which does not appear in given age_seq",file=sys.stderr)
            assert len(self.age_seq) > 1,"There is at most one time value"
        elif datatype == "lifetable":
            pass
        else:
            assert False, "undefined datatype: {}".format(datatype)
                    

        # init variables
        self.datatype  = datatype
        # based on actuarial variablesm except external 'a'
        self.lifetable = type('PureLifeTable',(object,),{"l":None,"d":None,"a":None})
        
        if self.datatype == "entry":
            self.transaction_to_lifetable(df)
        elif self.datatype == "lifetable":
            self.time_seq   = df.columns.tolist()
            assert len(self.time_seq) > 1,"There is at most one time value"
            
            self.time_seq       = df.columns.tolist()
            self.age_seq        = df.index.tolist()
            self.lifetable.l    = df
            self.__init_lifetable_d()

        self.__calculate_quit_rate()
        

    def plot_quit_trend(self):
        sns.heatmap(self.quit_rate, annot=True, fmt="f")
        

    def __transaction_to_lifetable(self,df):
        #stub
        self.lifetable.l = df

    def __init_lifetable_d(self):
        # after calculating l
        # quit number
        self.lifetable.d = pd.DataFrame({},columns=self.time_seq[:-1])
        for idx in range(len(self.age_seq)-1):
            quit_num = self.lifetable.l.iloc[idx].values[:-1] - self.lifetable.l.iloc[idx+1].values[1:]
            self.lifetable.d = self.lifetable.d.append(pd.Series(quit_num,name=self.lifetable.l.index[idx],index=self.lifetable.d.columns))

    def __calculate_quit_rate(self):
        # after calculating l and d
        dfs = self.lifetable
        # todo: speed up
        self.quit_rate = pd.DataFrame({},columns=list(map(str,self.age_seq[:-1])))
        for t_pred in self.time_seq[:-1]:
            arr_pred = dfs.l[t_pred].values
            arr_next = dfs.d[t_pred].values
            quit_rate = pd.Series([arr_next[idx]/arr_pred[idx] for idx in range(len(self.age_seq)-1)],name=t_pred,index=self.quit_rate.columns)
            self.quit_rate = self.quit_rate.append(quit_rate)
        
    def predict(self):
        return "a"

    def load_external(self,data):
        pass
        
        

    @classmethod
    def __trim(data):
        # stub
        return data

    

if __name__ == '__main__':
    pass
