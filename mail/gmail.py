from model.supermarket_product_model import SupermarketProduct
from functions.functions import build_body_to_messaje
from email.mime.multipart import MIMEMultipart
from scrap.diaMarket import DiaMarket
from configparser import ConfigParser
from email.mime.text import MIMEText
from log.logger import Log
import smtplib


# GLOBAL VALUES #
config = ConfigParser()
config.read('mail/config.ini')
logger = Log().get_logger(__name__)

USER_GMAIL = config['Gmail']['user_Gmail']
PASSWORD_GMAIL = config['Gmail']['password_Gmail']


def get_report_supermermarket_prices() -> str:
    """ Retorno el scraping de supermercados para el armado del cuerpo del email.

    :return: str
    """
    try:
        dia_market_products = DiaMarket().get_products_from_markets()
        body = build_body_to_messaje(dia_market_products)
        return body

    except Exception as e:
        logger.error(f'Error en el cuerpo del mensaje de respuesta,'
                     f' error: "{e}"')


def send_email_whit_report_products(addressee: str) -> None:
    """ Envio un mail con las ofertas de los productos de Supermercados
     al destinatario.

    :param addressee: str
    """
    try:
        BODY = get_report_supermermarket_prices()

        SUBJECT = 'OFERTA de Supermercados'

        msg = MIMEMultipart()
        msg['From'] = USER_GMAIL
        msg['To'] = ', '.join([addressee])
        msg['Subject'] = SUBJECT

        BODY = MIMEText(BODY)
        msg.attach(BODY)

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(USER_GMAIL, PASSWORD_GMAIL)
        smtpObj.sendmail(USER_GMAIL, addressee, msg.as_string())
        smtpObj.quit()
        logger.info(f'Se envio correctamente el reporte al email de:'
                    f' "{addressee}"')

    except Exception as e:
        logger.error(f'ERROR no se pudo enviar el reporte al email de:'
                     f' "{addressee}", error: "{e}"')
