from mail.gmail import send_email_whit_report_products
from controller.products_controller import Controller
from scrap.diaMarket import DiaMarket
from view.products_view import View


if __name__ == '__main__':
    controller = Controller(DiaMarket(), View())
    controller.show_supermarket_products()

    # Envio del email con el reporte de productos al "Destinatario"
    send_email_whit_report_products(addressee='addressee_example@gmail.com')
