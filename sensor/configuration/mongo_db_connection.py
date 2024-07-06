import pymongo
from sensor.constant.database import DATABASE_NAME
from certifi
ca = certifi.where()
class MongoDBClient:
    client = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                Mongo_db_url = "mongodb+srv://Choubey:shivamchoubey221033nsit@cluster0.66ldgap.mongodb.net/"
                MongoDBClient.client = pymongo.MongoClient(Mongo_db_url, tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e