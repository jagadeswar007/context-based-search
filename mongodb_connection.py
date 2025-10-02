import pymongo;

mongoClient= pymongo.MongoClient('mongo connection details')

# print(mongoClient.list_database_names())

dbList = mongoClient.list_database_names()

print(dbList)

# if "development" in dbList:
#     print("development db exists")

myDB = mongoClient["vector-search"]

colList = myDB.list_collection_names()

print(colList)

# if "vector_search" in colList:
#     print("collection exists")

myCollection = myDB["context-search"]

myData = {"test": "a long text for testing", "vectorEmbeddings": [1.20, -1.3]}

x= myCollection.insert_one(myData)

print(x.inserted_id)




