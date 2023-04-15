from api import app
from flask import Response, request

from api.services import user_service, review_service


@app.route("/users", methods=["GET"])
def find_users():
    args = request.args

    offset = args.get("offset", default=0, type=int)  # Limit = page size
    limit = args.get("limit", default=100, type=int)  # Offset = where to start
    df_users = user_service.find_all(offset, limit)

    return Response(df_users.to_json(orient="records"), mimetype="application/json")


@app.route("/users/<user_id>", methods=["GET"])
def find_user(user_id):
    df_user = user_service.find_one(user_id)
    return Response(df_user.to_json(orient="records"), mimetype="application/json")


@app.route("/users/<user_id>/reviews", methods=["GET"])
def find_user_reviews(user_id):
    args = request.args

    offset = args.get("offset", default=0, type=int)  # Limit = page size
    limit = args.get("limit", default=100, type=int)  # Offset = where to start

    df_reviews = review_service.find_by_user_id(user_id, offset, limit)
    return Response(df_reviews.to_json(orient="records"), mimetype="application/json")
