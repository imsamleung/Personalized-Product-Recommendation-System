from api.repositories import review_repository


def find_all():
    return review_repository.find_all()


def find_one(product_id, user_id):
    return review_repository.find_one(product_id, user_id)


def find_by_product_id(product_id):
    df_reviews = find_all()
    return df_reviews[df_reviews["product_id"] == product_id]


def find_by_user_id(user_id):
    df_reviews = find_all()
    return df_reviews[df_reviews["user_id"] == user_id]
