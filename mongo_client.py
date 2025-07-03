from pymongo import MongoClient
from decouple import config

mongo_uri = config('MONGO_URI')
mongo_db_name = config('MONGO_DB_NAME')

client = MongoClient(mongo_uri)
db = client[mongo_db_name]