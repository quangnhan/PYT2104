import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.za75n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client["sample_training"]
col = db["grades"]

doc = col.find_one()

for x in doc:
    print(x)
