from model.supermarket_product_model import SupermarketProduct
from abc import ABCMeta, abstractmethod


class SuperMarketScraping(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_products_from_markets(self) -> list[SupermarketProduct]:
        pass
