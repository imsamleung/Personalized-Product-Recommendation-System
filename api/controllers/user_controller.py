from api import app
from flask import Response

from api.services import user_service, review_service


@app.route("/users")
def find_users():
    return Response(
        user_service.find_all()[:100].to_json(orient="records"),
        mimetype="application/json",
    )


@app.route("/users/<user_id>")
def find_user(user_id):
    return Response(
        user_service.find_one(user_id).to_json(orient="records"),
        mimetype="application/json",
    )


@app.route("/users/<user_id>/reviews")
def find_user_reviews(user_id):
    return Response(
        review_service.find_by_user_id(user_id).to_json(orient="records"),
        mimetype="application/json",
    )
