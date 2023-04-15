from api.repositories import review_repository


def find_all(offset: int = None, limit: int = None):
    return review_repository.find_all(offset, limit)


def find_one(product_id, user_id):
    return review_repository.find_one(product_id, user_id)


def find_by_product_id(product_id, offset: int = None, limit: int = None):
    df_reviews = find_all(offset, limit)
    return df_reviews[df_reviews["product_id"] == product_id]


def find_by_user_id(user_id, offset: int = None, limit: int = None):
    df_reviews = find_all(offset, limit)
    return df_reviews[df_reviews["user_id"] == user_id]
