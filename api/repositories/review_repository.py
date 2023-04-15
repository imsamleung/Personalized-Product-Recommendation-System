from api.datasource import get_reviews


def find_all(offset: int = None, limit: int = None):
    df_reviews = get_reviews()

    if offset is not None:
        if offset < 0:
            offset = 0
        df_reviews = df_reviews[offset:]

    if limit is not None:
        if limit < 1:
            limit = 1
        if limit > len(df_reviews):
            limit = len(df_reviews)
        df_reviews = df_reviews[:limit]

    return df_reviews


def find_one(product_id, user_id):
    df_reviews = find_all()
    return df_reviews[
        df_reviews["product_id"] == product_id & df_reviews["user_id"] == user_id
    ]
