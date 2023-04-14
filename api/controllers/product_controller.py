from api import app
from api.services import product_service, review_service
from flask import Response, session, redirect, url_for


@app.route("/products")
def find_products():
    return Response(
        product_service.find_all()[:100].to_json(orient="records"),
        mimetype="application/json",
    )


@app.route("/products/<product_id>")
def find_product(product_id):
    return Response(
        product_service.find_one(product_id).to_json(orient="records"),
        mimetype="application/json",
    )


@app.route("/products/<product_id>/reviews")
def find_product_reviews(product_id):
    return Response(
        review_service.find_by_product_id(product_id).to_json(orient="records"),
        mimetype="application/json",
    )


@app.route("/products/<product_id>/recommend/proposed", methods=["GET"])
def recommend(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]

    df_products = product_service.recommend(user_id, product_id, 10)

    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route("/products/<product_id>/recommend/content-based-filtering", methods=["GET"])
def content_based_filtering(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]

    df_products = product_service.content_based_filtering(user_id, product_id, 10)

    return Response(df_products.to_json(orient="records"), mimetype="application/json")


@app.route(
    "/products/<product_id>/recommend/item-based-collaborative-filtering",
    methods=["GET"],
)
def item_based_collaborative_filtering(product_id):
    if "user_id" not in session:
        return redirect(url_for("find_users"))

    user_id = session["user_id"]

    df_products = product_service.item_based_collaborative_filtering(
        user_id, product_id, 10
    )

    return Response(df_products.to_json(orient="records"), mimetype="application/json")
