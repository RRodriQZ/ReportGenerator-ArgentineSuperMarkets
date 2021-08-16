from model.supermarket_product_model import SupermarketProduct
from unicodedata import normalize
from bs4 import BeautifulSoup
from log.logger import Log
import requests
import re
import urllib3

urllib3.disable_warnings()


# GLOBAL VALUES #
logger = Log().get_logger(__name__)


def get_response_by_url(url: str) -> BeautifulSoup:
    """Return the response of the call to the URL of the Supermarket

    :param url: str
    :return: BeautifulSoup
    """
    try:
        request = requests.get(url, verify=True)
        response = BeautifulSoup(request.content, "html.parser")
        return response

    except Exception as e:
        logger.error(f'Error returning the Response of url: "{url}", error: "{e}"')


def get_normalizer_title(title: str) -> str:
    """Return the title of the standardized product

    :param title: str
    :return: str
    """
    title = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
        r"\1",
        normalize("NFD", title),
        0,
        re.I,
    )
    title_formated = normalize("NFC", title)

    return title_formated


def get_name_product_normalized_market_dia(title: BeautifulSoup) -> str:
    """Return the name of the Scraping product associated with the Supermarket

    :param title: BeautifulSoup
    :return: str
    """
    name_of_product = title.h3.a.text.strip()
    name_of_product_normalized = get_normalizer_title(title=name_of_product)
    return name_of_product_normalized


def clean_product_value_market_dia(product: BeautifulSoup) -> float:
    """Return the clean value of the product

    :param product: BeautifulSoup
    :return: float
    """
    product = product.find("div", {"class": "price"}).span.text.strip()
    product_price_format = (product.split("$ ")[1]).replace(",", ".")

    return float(product_price_format)


def get_title_product_and_product_value(supermarket: str, value: BeautifulSoup) -> tuple[str, float]:
    """Return product associated with the Supermarket and value of the product

    :param supermarket: str
    :param value: BeautifulSoup
    :return: tuple[str, float]
    """
    try:
        if supermarket == "DIA":
            title_product = get_name_product_normalized_market_dia(title=value)
            product = clean_product_value_market_dia(product=value)

            return title_product, product
    except:
        pass


def build_body_to_messaje(products_DIA: list[SupermarketProduct]) -> str:
    """Return the body of the message in text format

    :param products_DIA: list[SupermarketProduct]
    :return: str
    """
    try:
        products_dia = [product.get_product() for product in products_DIA]
        prices_dia = [product.get_price() for product in products_DIA]

        body = ""
        body += "********************[ DIA ]********************" + "\n"
        for i in range(len(products_dia)):
            body += "* " + products_dia[i]
            body += "  -> $ " + str(prices_dia[i]) + "\n"

        return body

    except Exception as e:
        logger.error(f'Error in assembling the body of the message, error: "{e}"')
