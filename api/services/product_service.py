from api.repositories import product_repository
from api.services import recommendation_service


def find_all(offset: int = None, limit: int = None):
    return product_repository.find_all(offset, limit)


def find_one(product_id):
    return product_repository.find_one(product_id)


def recommend(user_id, product_id, n=10):
    return recommendation_service.recommend(user_id, product_id, n)


def content_based_filtering(user_id, product_id, n=10):
    return recommendation_service.content_based_filtering(user_id, product_id, n)


def item_based_collaborative_filtering(user_id, product_id, n=10):
    return recommendation_service.item_based_collaborative_filtering(
        user_id, product_id, n
    )
