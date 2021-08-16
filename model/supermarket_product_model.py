from dataclasses import dataclass


@dataclass
class SupermarketProduct(object):
    """Class represents SupermarketProduct model fields: market, product & price"""

    market: str
    product: str
    price: float

    def get_market(self) -> str:
        return self.market

    def get_product(self) -> str:
        return self.product

    def get_price(self) -> float:
        return self.price

    def __str__(self) -> str:
        return f"[MARKET]: {self.get_market()} [PRODUCT]: {self.get_product()} [PRICE]: $ {self.get_price()}"
