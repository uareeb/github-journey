from flask import Blueprint, request, jsonify
from models.user_store import create_user, get_all_users, get_user

user_bp = Blueprint("users", __name__, url_prefix="/api")

# GET all users
@user_bp.route("/users", methods=["GET"])
def fetch_users():
    return jsonify(get_all_users())

# GET single user
@user_bp.route("/users/<string:user_id>", methods=["GET"])
def fetch_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# POST create user
@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.json

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user = create_user(data["name"], data["age"],data["city"])
    return jsonify(user), 201
