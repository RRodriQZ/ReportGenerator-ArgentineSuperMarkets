from jsonschema import validate
import json
import os


def validate_products_for_schema(json_product: dict) -> None:
    file_path = os.path.join(os.path.dirname(__file__), 'product.json')
    with open(file_path, 'r') as values:
        SCHEMA_PRODUCTS = json.load(values)

    validate(instance=json_product, schema=SCHEMA_PRODUCTS)
