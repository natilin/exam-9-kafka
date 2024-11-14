import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv(verbose=True)

client = MongoClient(os.environ["MONGO_DB_URL"])
mongo_db = client["enemy_email"]
all_messages_collection = mongo_db["all_messages"]

def init_mongo_db():
    all_messages_collection.drop()