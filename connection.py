from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
def get_database():
    CONNECTION_STRING = os.getenv("CONNECTION_STRINGDB")
    client = MongoClient(CONNECTION_STRING)
    return client["Vaccines"]

if __name__=="__main__":
    dbname = get_database()



