from mail.gmail import send_email_whit_report_products
from controller.products_controller import Controller
from scrap.diaMarket_scraping import DiaMarketScraping
from view.products_view import View


def main() -> None:
    controller = Controller(DiaMarketScraping(), View())
    controller.show_supermarket_products()

    # Sending the email with the product report to the "addresse"
    send_email_whit_report_products(addressee="addressee_example@gmail.com")


if __name__ == "__main__":
    main()
