from abc import ABCMeta, abstractmethod


class SuperMarketScraping(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_products_from_markets(self) -> list:
        pass
