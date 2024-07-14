from pymongo.mongo_client import MongoClient

# MongoDB connection URI
uri = "mongodb+srv://pratice:123456aA@pratice.dxrjynw.mongodb.net/?retryWrites=true&w=majority&appName=pratice"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Ping successful. Connected to MongoDB.")
except Exception as e:
    print("An error occurred:", e)
