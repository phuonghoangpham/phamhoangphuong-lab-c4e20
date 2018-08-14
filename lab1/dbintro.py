from pymongo import MongoClient

mongo_uri = "mongodb://phphuong0912:Glasgowg128qq!@ds119088.mlab.com:19088/phuonghoangpham"

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

#4. Create a document
new_game = {
'title': 'LOL',
'description': 'League of Legend'
}

#5. Insert doc into collection
games.insert_one(new_game)

#6. Read all documents
all_games = games.find()
first_game = all_games[0]
print(first_game['description'])