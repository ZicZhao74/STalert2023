import pandas as pd
import os
import datetime
import time
import comfunc as cf


hislist, stock_nolist = cf.gethislist()
# print(hislist, stock_nolist)
path = os.getcwd()
print(path, '/112kdnewhistory/', hislist.iat[0, 0])
for i in range(0, 1):  # len(hislist)
    pf = pd.read_csv(path + '/112kdnewhistory/' + hislist.iat[i, 0])

    mean_volume = pf['成交股數'].tail(30).mean()
    print(mean_volume)

    # for x in range(0, len(pf)):
    #    print(pf.at[x, '成交股數'])

    # print(pf)
