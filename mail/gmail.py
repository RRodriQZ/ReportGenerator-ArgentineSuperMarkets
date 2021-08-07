from functions.functions import build_body_to_messaje
from email.mime.multipart import MIMEMultipart
from scrap.diaMarket import DiaMarketScraping
from configparser import ConfigParser
from email.mime.text import MIMEText
from log.logger import Log
import smtplib


# GLOBAL VALUES #
logger = Log().get_logger(__name__)

config = ConfigParser()
config.read("mail/config.ini")
USER_GMAIL = config["Gmail"]["user_Gmail"]
PASSWORD_GMAIL = config["Gmail"]["password_Gmail"]


def get_report_supermermarket_prices() -> str:
    """Return the scraping of supermarkets for the assembly of the body of the email

    :return: str
    """
    try:
        dia_market_products = DiaMarketScraping().get_products_from_markets()
        body = build_body_to_messaje(products_DIA=dia_market_products)
        return body

    except Exception as e:
        logger.error(f'Error en el cuerpo del mensaje de respuesta, error: "{e}"')


def send_email_whit_report_products(addressee: str) -> None:
    """Sended an email with the offers of the Supermarkets products
    to the recipient

    :param addressee: str
    """
    try:
        BODY = get_report_supermermarket_prices()

        SUBJECT = "SUPERMARKET OFFER"

        msg = MIMEMultipart()
        msg["From"] = USER_GMAIL
        msg["To"] = ", ".join([addressee])
        msg["Subject"] = SUBJECT

        BODY = MIMEText(BODY)
        msg.attach(BODY)

        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(USER_GMAIL, PASSWORD_GMAIL)
        smtpObj.sendmail(USER_GMAIL, addressee, msg.as_string())
        smtpObj.quit()

        logger.info(f'The report was successfully sent to the email of: "{addressee}"')

    except Exception as e:
        logger.error(
            f'ERROR the report could not be sent to the email of: "{addressee}", error: "{e}"'
        )
