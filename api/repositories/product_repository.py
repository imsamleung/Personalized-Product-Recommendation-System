from api.datasource import get_products


def find_all(offset: int = None, limit: int = None):
    df_products = get_products()

    if offset is not None:
        if offset < 0:
            offset = 0
        df_products = df_products[offset:]

    if limit is not None:
        if limit < 1:
            limit = 1
        if limit > len(df_products):
            limit = len(df_products)
        df_products = df_products[:limit]

    return df_products


def find_one(product_id):
    df_products = find_all()
    return df_products[df_products["product_id"] == product_id]
