from api.services import recommendation_service


def recommend(user_id, product_id, n=10):
    df_products = recommendation_service.recommend(user_id, product_id, n)
    return df_products[['product_id', 'name', 'price', 'image_url']]


def content_based_filtering(user_id, product_id, n=10):
    df_products = recommendation_service.content_based_filtering(
        user_id, product_id, n)
    return df_products[['product_id', 'name', 'price', 'image_url']]


def item_based_collaborative_filtering(user_id, product_id, n=10):
    df_products = recommendation_service.item_based_collaborative_filtering(
        user_id, product_id, n)
    return df_products[['product_id', 'name', 'price', 'image_url']]
