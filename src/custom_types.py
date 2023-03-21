import datetime
from typing import TypedDict


class Order:

    buy_price: str
    isSold: bool = False
    profit: int

    def __init__(self, buy_date, buy_price: float) -> None:
        self.buy_date = buy_date
        self.buy_price = buy_price
        self.isSold = False
        self.profit = 0

    def sell(self, date: datetime.date, price: float, profit: float):
        '''
        一筆交易賣出離場
        '''
        self.isSold = True
        self.profit = round(profit, 2)
        self.sell_date = date
        self.sell_price = price
        self.sell_on = 'close'
