import json
from flask import Flask, render_template, jsonify
import pymongo
from decouple import config
from bson.json_util import dumps

config.encoding = 'cp1251'
SECRET_KEY = config('SECRET_KEY')

app = Flask(__name__)

client = pymongo.MongoClient(SECRET_KEY)
db = client.Escuela
usuarios = db.alumno


@app.route('/')
def index():

    _cursor = usuarios.find({})
    list_cur = list(_cursor)
    json_data = dumps(list_cur)
    
    return json_data


if __name__ == '__main__':
    app.run(debug=True)
