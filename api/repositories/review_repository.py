from api.datasource import get_reviews


def find_all():
    return get_reviews()


def find_one(product_id, user_id):
    df_reviews = find_all()
    return df_reviews[
        df_reviews["product_id"] == product_id & df_reviews["user_id"] == user_id
    ]
