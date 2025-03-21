import pymongo                  #importing pymongo(struggled)
from pymongo import MongoClient  # importing mongoclient from pymongo library

cluster = MongoClient()             # linking the cluster  (local cluster because the atlas one is not working at all)
db = cluster["Test"]        #creating a database in the cluster and naming it 
Collection = db["TestC"]      #creating a collection inside the database and naming it

## Cluster is a space in cloud, Database is set of collections in the cloud and collection is kindoff mini database containing posts. Posts are bascically information posted in form of post lol
# Posts are in Json aka Dictionary Format {}



