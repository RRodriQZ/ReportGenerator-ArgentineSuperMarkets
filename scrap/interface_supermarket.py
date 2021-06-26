from model.supermarket_product_model import SupermarketProduct
from abc import ABCMeta, abstractmethod
from log.logger import Log


class SuperMarket(object):
    __metaclass__ = ABCMeta

    def __init__(self, log=Log()) -> None:
        self.logger = log.get_logger(__name__)

    @abstractmethod
    def get_products_from_markets(self) -> list[SupermarketProduct]: pass
