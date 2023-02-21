import pandas as pd
import requests
import json
import time
import random
import os
from datetime import datetime
import comfunc as cf


def urltjason(url):
    user_agent = {'User-agent': 'Chrome/107.0.0.0'}
    r = requests.get(url,  headers=user_agent)
    print(r, '狀態回應')
    list_of_dicts = r.json()
    # print (list_of_dicts)
    return (list_of_dicts)


def getstockdata(date, stock_no):
    html = urltjason(
        'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=%s' % (date, stock_no))
    stock_data = html['data']
    col_name = html['fields']
    global stockname
    stockname = html['title']
    return pd.DataFrame(data=stock_data, columns=col_name)


def historydata(date, enddate, stockdata, stock_no):
    for i in range(1, 5):  # 累積<5年資料
        for j in range(1, 13):
            print(date)
            stockdata = stockdata.append(getstockdata(date, stock_no))
            time.sleep(random.uniform(3, 6))
            date = date + 100
            if date > enddate:
                break
        date = date + 10000 - 1200
        if date > enddate:
            break
    return stockdata


def makehistorylist(historylistdir):
    # 建立歷史資料檔名列表historylist
    historylistdir = historylistdir
    historylist = pd.DataFrame(os.listdir(historylistdir))
    print(historylist)
    historylist.to_csv("historylist.csv", index=False, encoding='utf-8-sig')


# 要更新的月份
# date = 20230101
path = os.getcwd()
# 歷史檔案清單與清單內股票代號
hislist = pd.read_csv(path+'/historylist.csv', encoding='utf-8-sig')
stock_nolist = []
for i in range(0, len(hislist)):  # len(hislist)
    hislists = hislist.iat[i, 0].split()
    # print (hislists,hislists[1])
    stock_nolist.append(hislists[1])
stock_nolist = pd.DataFrame(stock_nolist)

for i in range(0, len(hislist)):  # len(hislist)

    # 取得自有歷史資料
    thehistory = pd.read_csv(path+'/112kdnewhistory/' +
                             hislist.iat[i, 0])
    print(hislist.iat[i, 0])
    print(thehistory)
    thehistory.drop(thehistory.columns[thehistory.columns.str.contains(
        'unnamed', case=False)], axis=1, inplace=True)
    thehistory.drop(thehistory.columns[thehistory.columns.str.contains(
        '0', case=False)], axis=1, inplace=True)

    net = ['成交股數', '成交金額', '開盤價']
    thehistory.drop_duplicates(subset=net, keep='first', inplace=True)
    # for j in range(0, len(thehistory)):
    #    thehistory.at[j, '日期'] = cf.datetoTWslash(thehistory.at[j, '日期'])
    # print(thehistory)
    thehistory.to_csv(path+'/112kdnewhistory/' +
                      hislist.iat[i, 0], index=False, encoding='utf-8-sig')
'''

    thehistory.reset_index(drop=True, inplace=True)
    print(thehistory)
    thehistory.to_csv(path+'/112newhistory/' +
                      hislist.iat[i, 0], index=False, encoding='utf-8-sig')

    thehistory.set_index(pd.to_datetime(
        thehistory['日期'], format='%Y/%m/%d'), inplace=True)
    print(type(thehistory['日期']))
    thehistory.sort_index()
    print(thehistory.tail(15))
    thehistory = thehistory.sort_values(by='日期')
    print(thehistory.tail(15))
    '''
