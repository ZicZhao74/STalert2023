from typing import TypedDict


class Order:

    buy_price: str
    isSold: bool = False
    profit: int

    def __init__(self, buy_price) -> None:
        self.buy_price = buy_price
        self.isSold = False
