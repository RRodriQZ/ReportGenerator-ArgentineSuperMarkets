class SupermarketProduct(object):
    def __init__(self, market: str, product: str, price: float) -> None:
        self._market = market
        self._product = product
        self._price = price

    def get_market(self) -> str:
        return self._market

    def get_product(self) -> str:
        return self._product

    def get_price(self) -> float:
        return self._price

    def __str__(self) -> str:
        return f'[MARKET]: "{self.get_market()}" ' \
               f'[PRODUCT]: "{self.get_product()}" ' \
               f'[PRICE]: $ {self.get_price()}'
