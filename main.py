import pymongo                  #importing pymongo(struggled)
from pymongo import MongoClient  # importing mongoclient from pymongo library

cluster = MongoClient("mongodb://localhost:27017/")   # linking the cluster  (local cluster because the atlas one is not working as of now)
db = cluster["Test2"]        #creating a database in the cluster and naming it 
collection = db["TestC"]      #creating a collection inside the database and naming it

## Cluster is a space in cloud, Database is set of collections in the cloud and collection is kindoff mini database containing posts. Posts are bascically information posted in form of post lol
# Posts are in Json(aka Dictionary) Format {key:Value} # posts always have this _id: tag this id is how we access these posts

 # post = {"_id":1, "name": "Bharadwaj", "favNum": 29 } # _id will be automatically generated if not guven in our code
 # collection.insert_one(post)
# after this it will create a post according to post of id:1 and we can check in mongodb Compass 


