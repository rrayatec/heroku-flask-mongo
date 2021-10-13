from flask import Flask, render_template
import pymongo
from decouple import config

config.encoding = 'cp1251'
SECRET_KEY = config('SECRET_KEY')

app = Flask(__name__)


@app.route('/')
def index():

    client = pymongo.MongoClient(SECRET_KEY)
    db = client.Escuela
    usuarios = db.alumno
    return SECRET_KEY


if __name__ == '__main__':
    app.run(debug=True)
