
from ast import List
import json
import pandas as pd
import os
from custom_types import Order

from indexs import kd_passavation

SELL_RATION_THRESHOLD = 0.07


def checkStrategyPass(index, rule):

    return False


def backTest(target, data: pd.DataFrame, strategies):
    orders: List[Order] = []
    for index, d in data.iterrows():
        for strategy in strategies:
            if strategy(data, index) is False:
                break
            orders.append(Order(
                data.at[index+1, '開盤價'],
            ))
        if len(orders) == 0:
            continue
        last_orders = filter(lambda order: order.isSold is False, orders)
        for order in last_orders:
            # print(json.dumps(last_order.__dict__))
            if order and order.isSold is False:
                price_diff = d['收盤價'] - order.buy_price
                price_diff_ratio = price_diff / order.buy_price
                if abs(price_diff_ratio) > SELL_RATION_THRESHOLD:
                    order.isSold = True
                    order.profit = price_diff
    print(json.dumps([o.__dict__ for o in orders], sort_keys=True, indent=4))
    # for order in orders:
    #     pass


if __name__ == '__main__':
    # 讀取歷史資料檔名列表
    stockList = pd.read_csv('historylist.csv', thousands=',')

    print(os.getcwd())
    for index, stock in stockList.iterrows():
        print(stock[0])
        history_data = pd.read_csv(
            os.getcwd()+'/112kdnewhistory/'+stock[0], thousands=',')
        backTest(stock, history_data, [kd_passavation])
