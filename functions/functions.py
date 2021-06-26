from model.supermarket_product_model import SupermarketProduct
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings()


def get_response_by_url(url: str) -> BeautifulSoup:
    """ Retorno el response del llamado a la URL del Supermercado.

    :param url: str
    :return: BeautifulSoup
    """
    try:
        request = requests.get(url, verify=True)
        response = BeautifulSoup(request.content, 'html.parser')
        return response

    except Exception as e:
        logger.error(f'Error al devolver el Response de url: "{url}",'
                     f' error: "{e}"')


def get_name_product(supermarket: str, title: BeautifulSoup) -> str:
    """ Retorno el nombre del producto del Scraping asociado al Supermercado.

    :param supermarket: str
    :param title: BeautifulSoup
    :return: str
    """
    try:
        if supermarket == 'DIA':
            title_product = title.h3.a.text.strip()
            return title_product

    except Exception as e:
        logger.error(f'Error en el nombre del producto del supermercado: '
                     f'"{supermarket}", error: "{e}"')


def clean_product_value(supermarket: str, value: BeautifulSoup) -> float:
    """ Retorno el valor limpio del producto.

    :param supermarket: str
    :param value: BeautifulSoup
    :return: float
    """
    try:
        if supermarket == 'DIA':
            product = value.find('div', {'class': 'price'}).span.text.strip()
            product_price_format = (product.split('$ ')[1]).replace(",", ".")

            return float(product_price_format)

    except Exception as e:
        logger.error(f'Error en el retorno del valor del producto: '
                     f'"{supermarket}", error: "{e}"')


def build_body_to_messaje(products_DIA: list[SupermarketProduct]) -> str:
    """ Retorno el cuerpo del mensaje en formato de texto.

    :param products_DIA: list[SupermarketProduct]
    :return: str
    """
    try:
        products_dia = [product.get_product() for product in products_DIA]
        prices_dia = [product.get_price() for product in products_DIA]

        body = ''
        body += '********************[ DIA ]********************' + '\n'
        for i in range(len(products_dia)):
            body += '* ' + products_dia[i]
            body += '  -> $ ' + str(prices_dia[i]) + '\n'

        return body

    except Exception as e:
        logger.error(f'Error en el armado del cuerpo del mensaje, error: "{e}')
