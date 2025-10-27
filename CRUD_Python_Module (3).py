#CRUD_Python_Module.py

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user='aacuser', password='Ji1234', host='localhost', port=27017, db='aac', col='animals'):
      
        # Initialize Connection
        uri = f'mongodb://{user}:{password}@{host}:{port}/{db}?authSource=admin'
        self.client = MongoClient(uri)
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        """Insert a document into the MongoDB database."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, criteria=None):
        """Query documents from the MongoDB database."""
        criteria = criteria or {}
        try:
            documents = self.collection.find(criteria)
            return list(documents)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
    def update(self, query, update_data, multiple=False):
        """Update document(s) in the collection"""
        try:
            if multiple:
                result = self.collection.update_many(query, {'$set': update_data})
            else:
                result = self.collection.update_one(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            print(f"Update Error: {e}")
            return []

    def delete(self, query, multiple=False):
        """Delete document(s) from the collection"""
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete Error: {e}")
            return []
def read_water_rescue(self):
    return self.collection.find({"rescue_type": "Water Rescue"})

def read_mountain_rescue(self):
    return self.collection.find({"rescue_type": {"$in": ["Mountain Rescue", "Wilderness Rescue"]}})

def read_disaster_tracking(self):
    return self.collection.find({"rescue_type": "Disaster or Individual Tracking"})