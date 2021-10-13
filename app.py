from flask import Flask, render_template
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://rraya:rubenraya@cluster0.w9ojs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
