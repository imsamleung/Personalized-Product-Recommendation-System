from api.datasource import get_products


def find_all():
    return get_products()


def find_one(product_id):
    df_products = find_all()
    return df_products[df_products["product_id"] == product_id]
