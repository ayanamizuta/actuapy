

# create trucated table
# input: pandas.core.frame.DataFrame
#  like
# column  2016 2017 2018 2019  (not only years, but day, month etc...)
# 10      100  200  300  400
# 11      200  200  200  200
# 12      300  300  300  300
#
# output: 10_live 10_quit 11_quit
# 2016    100             
#  
def truncated_table(df: DataFrame):
    
    
