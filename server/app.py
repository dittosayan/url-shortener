from flask import Flask,redirect,request,Response
from datetime import datetime
import requests
from pymongo import MongoClient
import json
app = Flask(__name__)

host = "127.0.0.1"
port= 5000

conn = MongoClient('mongodb+srv://ghosty:ghosty@cluster0.cuaqq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
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

    
    return str(host)+(":")+str(port)+"/r"+str(key)

@app.route('/r/<key>')
def red(key):
    
    resp = map_col.find_one({"key": str(key)})
    if resp!= None:
        return redirect("http://"+str(resp["url"]))
    return "Not Registered"
if __name__ == '__main__':
    
    app.run(host=host, port=port, debug=True)
