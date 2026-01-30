from bson import ObjectId
from db.database import user_collection
import logging

# CREATE USER
def create_user(name, age,city):
    user = {"name": name, "age": age,"city":city}
    result = user_collection.insert_one(user)
    logging.info(f"User created with ID {result.inserted_id}")
    user["_id"] = str(result.inserted_id)
    return user

# GET ALL USERS
def get_all_users():
    users = []
    for user in user_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    logging.info("Fetched all users")
    return users

# GET SINGLE USER
def get_user(user_id):
    try:
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
        return user
    except Exception:
        logging.error("Invalid user ID format")
        return None
