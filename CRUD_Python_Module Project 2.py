from pymongo import MongoClient 
from bson.objectid import ObjectId 


class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'Swifyfunf' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d?authSource=admin' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Insert error: {e}")
                return False
        else:
            raise ValueError("Data cannot be empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if isinstance(query, dict):
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print(f"Read error: {e}")
                return []
        else:
            raise ValueError("Query must be a dictionary")

    # Create method to implement the U in CRUD.
    def update(self, query, new_values):
        if isinstance(query, dict) and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print(f"Update error: {e}")
                return 0
        else:
            raise ValueError(
                "Query and update values must be dictionaries"
            )

    # Create method to implement the D in CRUD.
    def delete(self, query):
        if isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Delete error: {e}")
                return 0
        else:
            raise ValueError("Query must be a dictionary")