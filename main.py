from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)

conn = 'mongodb://127.0.0.1:27017/Users'
client = MongoClient(conn)
db = client['contactmanager']
collection_name = db["contacts"]


@app.route('/add_contact', methods=['POST'])
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = collection_name.insert_one({
                "name": user_name,
                "contact": user_contact
            })
        return dumps({'Message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})


@app.route('/contacts', methods=['GET'])
def get_all_contacts():
    try:
        contacts = collection_name.find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error': str(e)})
