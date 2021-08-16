from schemas.supermarket_product_schema import SupermarketProductSchema
from model.supermarket_product_model import SupermarketProduct
from scrap.interface_supermarket import SuperMarketScraping
from functions.decorators import singleton
from dataclasses import dataclass
from functions.functions import (
    get_response_by_url,
    get_title_product_and_product_value,
)
from log.logger import Log


@singleton
@dataclass
class DiaMarketScraping(SuperMarketScraping):
    """Class represents DiaMarketScraping fields: market, logger & url"""

    market: str = "DIA"
    logger: Log = Log().get_logger(__name__)
    url: str = "https://diaonline.supermercadosdia.com.ar/especial-ofertas"

    def get_products_from_markets(self) -> list[SupermarketProduct]:
        product_list: list[SupermarketProduct] = []
        response = get_response_by_url(url=self.url)

        self.logger.info(f"******************[ SCRAPING STARTED ]******************")

        for market_value in response.find_all("li"):
            try:
                product_name, product_price = get_title_product_and_product_value(
                    supermarket=self.market, value=market_value
                )

                new_product: SupermarketProduct = SupermarketProductSchema().load(
                    {
                        "market": self.market,
                        "product": product_name,
                        "price": product_price,
                    }
                )

                product_list.append(new_product)

                self.logger.info(
                    f'* The product was correctly extracted: "{new_product.__str__()}"'
                )

            except:
                pass

        return product_list
