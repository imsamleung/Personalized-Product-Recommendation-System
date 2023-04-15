from api import app
from api.services import product_service, review_service
from flask import Response, request, session, redirect, url_for


@app.route("/products", methods=["GET"])
def find_products():
    args = request.args

    offset = args.get("offset", default=0, type=int)  # Limit = page size
    limit = args.get("limit", default=100, type=int)  # Offset = where to start
    df_products = product_service.find_all(offset, limit)
    df_products = df_products[["product_id", "name", "price", "image_url"]]

    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route("/products/<product_id>", methods=["GET"])
def find_product(product_id):
    df_products = product_service.find_one(product_id)
    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route("/products/<product_id>/reviews", methods=["GET"])
def find_product_reviews(product_id):
    args = request.args

    offset = args.get("offset", default=0, type=int)  # Limit = page size
    limit = args.get("limit", default=100, type=int)  # Offset = where to start

    df_reviews = review_service.find_by_product_id(product_id, offset, limit)
    return Response(df_reviews.to_json(orient="records"), mimetype="application/json")


@app.route("/products/<product_id>/recommend/proposed", methods=["GET"])
def recommend(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]
    n = request.args.get("n", default=10, type=int)

    df_products = product_service.recommend(user_id, product_id, n)
    df_products = df_products[["product_id", "name", "price", "image_url"]]

    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route("/products/<product_id>/recommend/content-based-filtering", methods=["GET"])
def content_based_filtering(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]
    n = request.args.get("n", default=10, type=int)

    df_products = product_service.content_based_filtering(user_id, product_id, n)
    df_products = df_products[["product_id", "name", "price", "image_url"]]

    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route(
    "/products/<product_id>/recommend/item-based-collaborative-filtering",
    methods=["GET"],
)
def item_based_collaborative_filtering(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]
    n = request.args.get("n", default=10, type=int)

    df_products = product_service.item_based_collaborative_filtering(
        user_id, product_id, n
    )
    df_products = df_products[["product_id", "name", "price", "image_url"]]

    return Response(df_products.to_json(orient="records"), mimetype="application/json")
