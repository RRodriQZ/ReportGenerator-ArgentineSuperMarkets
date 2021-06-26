class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_supermarket_products(self):
        product_prices = self.model.get_products_from_markets()

        markets = [product.get_market() for product in product_prices]
        products = [product.get_product() for product in product_prices]
        prices = [product.get_price() for product in product_prices]

        self.view.show_market_prices(markets, products, prices)
