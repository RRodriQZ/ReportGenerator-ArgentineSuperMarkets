from model.supermarket_product_model import SupermarketProduct
from marshmallow import Schema, fields, post_load


class SupermarketProductSchema(Schema):
    """SupermarketProduct Schema"""

    market = fields.String(attribute="market")
    product = fields.String(attribute="product")
    price = fields.Float(attribute="price")

    @post_load
    def create_product(self, data, **kwargs):
        return SupermarketProduct(**data)
