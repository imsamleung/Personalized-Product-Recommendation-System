from api import app
from api.services import product_service
from flask import Response


@app.route('/users/<user_id>/products/<product_id>/recommend/proposed', methods=['GET'])
def recommend(user_id, product_id):
    df_products = product_service.recommend(user_id, product_id, 10)
    return Response(df_products.to_json(orient="records"), mimetype='application/json')

@app.route('/users/<user_id>/products/<product_id>/recommend/content-based-filtering', methods=['GET'])
def content_based_filtering(user_id, product_id):
    df_products = product_service.content_based_filtering(user_id, product_id, 10)
    return Response(df_products.to_json(orient="records"), mimetype='application/json')

@app.route('/users/<user_id>/products/<product_id>/recommend/item-based-collaborative-filtering', methods=['GET'])
def item_based_collaborative_filtering(user_id, product_id):
    df_products = product_service.item_based_collaborative_filtering(user_id, product_id, 10)
    return Response(df_products.to_json(orient="records"), mimetype='application/json')
