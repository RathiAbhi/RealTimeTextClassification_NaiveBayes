"""
This file imports/fetches the raw data from mongoDB that has been
collected from the resources
"""

import json
from pymongo import MongoClient
from config import MONGO_DB,MONGO_URI,MONGO_COLLECTIONS

class DataFetcher():
    def fetch_from_mongo(self):
        "Fetches data from mongodb"
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]
        collections = db[MONGO_COLLECTIONS]
        return list(collections.find({},{"_id":0})) #Excludes Id

    @staticmethod
    def fetch_from_json(file_path):
        """
        Loads data from a json file
        A static method belongs to the class, not to the
        instance of that class.
        """
        with open(file_path,"r") as file:
            return json.load(file)