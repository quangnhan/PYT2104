import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.jn5hm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["sample_training"]
col = db["grades"]

doc = col.find_one()

for x in doc:
    print(x)