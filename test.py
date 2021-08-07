from scrap.diaMarket_scraping import DiaMarketScraping
import unittest


class MarketProducts(unittest.TestCase):
    def setUp(self):
        self.product_list = []
        self.market = DiaMarketScraping()
        self.market_products = self.market.get_products_from_markets()

    def tearDown(self):
        pass

    def test_market_products_list_is_zero(self):
        length_product_list = len(self.product_list)
        self.assertEqual(length_product_list, 0)

    def test_types_market_dia_products(self):
        markets = [product.get_market() for product in self.market_products]
        products = [product.get_product() for product in self.market_products]
        prices = [product.get_price() for product in self.market_products]
        self.assertEqual(type(markets[0]), str)
        self.assertEqual(type(products[0]), str)
        self.assertEqual(type(prices[0]), float)

    def test_market_products_list_not_is_zero(self):
        self.product_list.extend(self.market_products)
        length_product_list = len(self.product_list)
        self.assertNotEqual(length_product_list, 0)


if __name__ == "__main__":
    unittest.main()
