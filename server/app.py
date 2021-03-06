from flask import Flask,redirect,request,Response
from datetime import datetime
import requests
from pymongo import MongoClient
import json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

host = "0.0.0.0"
port = os.getenv("PORT", 5000)

connection_s = os.getenv("mongo_con")
conn = MongoClient(connection_s)
db = conn["url-shortner"]
key_col = db["keys"]
map_col = db["maps"]

@app.route('/', methods=['POST'])
def shorten():
    response = request.data
    obj = json.loads(response)
    url = obj['url']

    

    key = key_col.find_one()
    key = key["key"]
    print(key)

    myquery = { "key": str(key) }
    key_col.delete_one(myquery)

    mapping = {"url": "",
               "key": ""
                }
    
    mapping["url"]=str(url)
    mapping["key"]=str(key)

    res = map_col.insert_one(mapping)

    
    return "https://peepee-url.herokuapp.com"+"/r/"+str(key)

@app.route('/r/<key>')
def red(key):
    
    resp = map_col.find_one({"key": str(key)})
    if resp!= None:
        return redirect("http://"+str(resp["url"]))
    return "Not Registered"
if __name__ == '__main__':
    
    app.run(host=host, port=port, debug=True)
