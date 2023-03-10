import pandas as pd
import requests
import json
import time
import random
import os


def urltjason(url):
    user_agent = {'User-agent': 'Chrome/107.0.0.0'}
    r = requests.get(url,  headers=user_agent)
    print(r, '狀態回應')
    list_of_dicts = r.json()
    # print (list_of_dicts)
    return (list_of_dicts)


def getstockdata(start_date, stock_no):
    html = urltjason(
        'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=%s' % (start_date, stock_no))
    print(html)
    stock_data = html['data']
    col_name = html['fields']
    global stockname
    stockname = html['title']
    return pd.DataFrame(data=stock_data, columns=col_name)


def historydata(start_date, end_date, stockdata, stock_no):
    for i in range(1, 5):  # 累積<5年資料
        for j in range(1, 13):
            print(start_date)
            stockdata = stockdata.append(getstockdata(start_date, stock_no))
            time.sleep(random.uniform(3, 6))
            start_date = start_date + 100
            if start_date > end_date:
                break
        start_date = start_date + 10000 - 1200
        if start_date > end_date:
            break
    return stockdata


def makehistorylist(historylistdir):
    # 建立新的股票追蹤列表 (by檔名)
    historylist = pd.DataFrame(os.listdir(historylistdir))
    # print(historylist)
    historylist.to_csv("historylist2.csv", index=False, encoding='utf-8-sig')


def getStockHis(path, start_date, end_date, stocklist):
    for i in range(0, len(stocklist)):
        print(stocklist.iat[i, 0])
        stock_no = stocklist.iat[i, 0]
        print('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=%s' %
              (start_date, stock_no))
        # CALL API取得資料後刪除，留下欄位
        stockdata = getstockdata(start_date, stock_no)
        stockdata.drop(stockdata.index)
        time.sleep(random.uniform(3, 6))
        # 依日期、結束、起始、股票號碼取得歷史資料
        stockdata = historydata(start_date, end_date, stockdata, stock_no)

        filename = stockname + '.csv'
        stockdata.to_csv(path+'/historydata/'+filename,
                         index=False, encoding='utf-8-sig')


# 基本參數、欄位取得
path = os.getcwd()
start_date = 20220301
end_date = 20220401
following_stocks = "STOCKLIST2.csv"
stocklist = pd.read_csv(following_stocks, dtype={'stocknum': str})
getStockHis(path, start_date, end_date, stocklist)
# 建立新的股票追蹤列表 (by檔名)
stockfilelist_dir = path+'/historydata/'
stockfilelist_name = 'stockfile_list.csv'
makehistorylist(stockfilelist_dir)
