print("I'm in settings file")
from pymongo.mongo_client import MongoClient

from dotenv import dotenv_values
from pymongo import MongoClient
config = dotenv_values(".env")
client=MongoClient(config["ATLAS_URI"])
db=client[config["DB_NAME"]]
userCollection = db["users"]
try:
    client.admin.command("ping")
    print("successfully connected to database using MongoDb!")
except Exception as e:
    print(e)

def hello():
    return "Hello world"