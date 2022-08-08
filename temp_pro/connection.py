import pymongo

client = pymongo.MongoClient("mongodb+srv://raytech:rayray123@cluster0.sviy3o6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)