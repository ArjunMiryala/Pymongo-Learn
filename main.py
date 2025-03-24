import pymongo                  #importing pymongo(struggled)
from pymongo import MongoClient  # importing mongoclient from pymongo library

cluster = MongoClient("mongodb://localhost:27017/")   # linking the cluster  (local cluster because the atlas one is not working as of now)
db = cluster["Test2"]        #creating a database in the cluster and naming it 
collection = db["TestC"]      #creating a collection inside the database and naming it

## Cluster is a space in cloud, Database is set of collections in the cloud and collection is kindoff mini database containing posts. Posts are bascically information posted in form of post lol
# Posts are in Json(aka Dictionary) Format {key:Value} # posts always have this _id: tag this id is how we access these posts

post = {"_id":1, "name": "Bharadwaj", "favNum": 29 } # _id will be automatically generated if not guven in our code
 # collection.insert_one(post)
# after this it will create a post according to post of id:1 and we can check in mongodb Compass 

post2 = {"_id":2 , "name" : "Koutiya", "favNum": 8}
post3 = {"_id":3 , "name": "PrabhaDevi", "favNum": 3}
post4 = {"_id": 4 , "name": "Jagadeshweer", "favNum": 2}

# collection.insert_many([post2, post3, post4])  # insert_many for insering multiple posts

# TO FIND INFORMATION

results = collection.find({"name": "Bharadwaj"})   
#This line queries the collection for all documents where the field "name" is exactly "Bharadwaj" and stores the cursor (not the actual documents yet) into the variable results.
#We can loop through it to access the documents:


for result in results:          #looping through results(cursor object)
    print(result)
    print(result["_id"])        # We can also access the individual elements of that post, example accessing id

results_id = collection.find({"_id":1}) # searching by id 

for result in results_id:
    print(result)

