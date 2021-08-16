class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_supermarket_products(self):
        product_prices: list = self.model.get_products_from_markets()

        markets: list[str] = [product.get_market() for product in product_prices]
        products: list[str] = [product.get_product() for product in product_prices]
        prices: list[float] = [product.get_price() for product in product_prices]

        self.view.show_market_prices(
            market_names=markets, market_products=products, market_prices=prices
        )
