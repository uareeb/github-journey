
from pymongo import MongoClient
import certifi
import logging

logging.basicConfig(level=logging.INFO)

MONGO_URI = "mongodb+srv://willop918_db_user:Default#147@cluster0.uy3ftc6.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsCAFile=certifi.where()
    )
    client.admin.command("ping")
    logging.info("✅ Connected to MongoDB Atlas")
except Exception as e:
    logging.error("❌ MongoDB Atlas connection failed", exc_info=True)
    raise e

db = client["rest_api"]
user_collection = db["users"]
