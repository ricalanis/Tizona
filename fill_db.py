from pymongo import MongoClient
import subprocess
import json
import os

client = MongoClient()
db = client.test

def generate_current():
    filename = "data/items_subprocess.json"
    try:
        os.remove(filename)
    except OSError:
        pass
    subprocess.call('scrapy crawl precio -o data/items_subprocess.json'.split(), stdout=subprocess.PIPE)
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def insert_mongo(datastream):
    for document in datastream:
        db.db_precios.insert(document)
    return "OK"

def main():
    client = MongoClient()
    db = client.test
    datastream = generate_current()
    insert_mongo(datastream)
    return "OK"

if __name__ == "__main__":
    main()
