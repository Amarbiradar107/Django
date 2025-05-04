from pymongo import MongoClient
client = MongoClient('cluster0-shard-00-01.y0xhb.mongodb.net:27017')
db = client['test']