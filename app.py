from flask import Flask, render_template
import pymongo

app = Flask(__name__)


@app.route('/')
def index():
    client = pymongo.MongoClient(
    "mongodb+srv://rraya:rubenraya@cluster0.w9ojs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.Escuela
    usuarios = db.alumno

    return render_template('index.html')





if __name__ == '__main__': app.run(debug=True)