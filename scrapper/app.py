from pymongo import MongoClient
from flask import Flask, Response, request, jsonify
import simplejson as json

app = Flask(__name__)

client = MongoClient()
db = client.test

def document_result(cursor):


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
app.after_request(add_cors_headers)

@app.route('/state', methods=['GET'])
def api_state():
    data = load_cities_data()
    json_data = json.dumps(data)
    cursor = db.test_cities.find( {"$and": [ { "city": city_name}, { "name": indicator_name } ] } )

    return Response(jsonify(json_fixed), mimetype='application/json')
