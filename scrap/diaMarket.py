from model.supermarket_product_model import SupermarketProduct
from scrap.interface_supermarket import SuperMarketScraping
from schemas.validate import validate_products_for_schema
from functions.decorators import singleton
from functions.functions import (
    get_response_by_url,
    clean_product_value,
    get_name_product_normalized
)
from log.logger import Log


@singleton
class DiaMarketScraping(SuperMarketScraping):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Log().get_logger(__name__)
        self.url = "https://diaonline.supermercadosdia.com.ar/especial-ofertas"

    def get_products_from_markets(self) -> list[SupermarketProduct]:
        product_list = []
        market_DIA = "DIA"

        response = get_response_by_url(url=self.url)

        self.logger.info(
            f"******************[ SCRAPING STARTED ]******************"
        )

        for market_value in response.find_all("li"):
            try:
                product_name = get_name_product_normalized(supermarket=market_DIA, title=market_value)
                product_price = clean_product_value(market_DIA, value=market_value)

                product_json: dict[str, str, float] = {
                    "market_name": market_DIA,
                    "product": product_name,
                    "price": product_price,
                }

                validate_products_for_schema(product_json)

                new_product = SupermarketProduct(
                    market_DIA, product_name, product_price
                )

                product_list.append(new_product)

                self.logger.info(
                    f'* The product was correctly extracted: "{new_product.__str__()}"'
                )

            except:
                pass

        return product_list
