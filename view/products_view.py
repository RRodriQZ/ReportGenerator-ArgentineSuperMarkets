class View(object):
    @staticmethod
    def show_market_prices(market_names, market_products, market_prices):
        for i in range(len(market_names)):
            print(f'* "Supermarket":  "{market_names[i]}"')
            print(f'* "Product":      "{market_products[i]}"')
            print(f'* "Price":        $ {market_prices[i]}')
            print(f"*********************************************************")
