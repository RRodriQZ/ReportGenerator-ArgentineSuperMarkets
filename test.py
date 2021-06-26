from scrap.diaMarket import DiaMarket
import unittest


class MarketProducts(unittest.TestCase):
    def setUp(self):
        self.product_list = []
        self.market = DiaMarket()
        self.market_products = self.market.get_products_from_markets()

    def tearDown(self):
        pass

    def testMarketProductsListIsZero(self):
        length_product_list = len(self.product_list)
        self.assertEqual(length_product_list, 0)

    def testTypesMarketDiaProducts(self):
        markets = [product.get_market() for product in self.market_products]
        products = [product.get_product() for product in self.market_products]
        prices = [product.get_price() for product in self.market_products]
        self.assertEqual(type(markets[0]), str)
        self.assertEqual(type(products[0]), str)
        self.assertEqual(type(prices[0]), float)

    def testMarketProductsListNotIsZero(self):
        self.product_list.extend(self.market_products)
        length_product_list = len(self.product_list)
        self.assertNotEqual(length_product_list, 0)


if __name__ == '__main__':
    unittest.main()
