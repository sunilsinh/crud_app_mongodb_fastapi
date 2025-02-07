# Importing the 'pymongo' module for MongoDB interaction
import pymongo

# Try to create a MongoDB client and connect to the server
try:
    # Creating a MongoClient to connect to the local MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Selecting a specific database named 'your_database_name'
    database = client["mydb"]

    # Printing a message indicating a successful connection
    print("Connected to MongoDB")

except Exception as e:
    # Handling exceptions and printing an error message if connection fails
    print(f"Error: {e}")