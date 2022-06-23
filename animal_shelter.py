from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:34570' % (username, password))
        
        self.database = self.client['project']
    
    
                            ########## CRUD Methods ##########
        
    # Create -- data must be in the form of a dictionary.
    def create(self, data=dict()):
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty.")
          
        
    # Read
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data, { "_id" : False })
        else:
            raise Exception("Nothing to return, because data parameter is empty.")
          
        
    # Update
    def update(self, find=dict(), replace=dict()):
        if find is not None:
            x = self.database.animals.update_many(find, {"$set" : replace})
            return json.dumps(str(x.modified_count) + ' records updated.')
        else:
            raise Exception("Nothing to update, because data parameter is empty.")
            
            
    # Delete
    def delete(self, data=dict()):
        if data is not None:
            return json.dumps(self.database.animals.remove(data), indent = 4)
        else:
            raise Exception("Nothing to delete, because data parameter is empty.")
            
            
            
            
