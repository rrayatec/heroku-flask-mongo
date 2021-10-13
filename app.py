from flask import Flask, redirect, url_for, request, render_template
import pymongo
from decouple import config
from bson.json_util import dumps

config.encoding = 'cp1251'
SECRET_KEY = config('SECRET_KEY')

app = Flask(__name__)

client = pymongo.MongoClient(SECRET_KEY)
db = client.Escuela
cuentas = db.alumno


@app.route('/')
def index():
    return render_template("/LoginFull.html")


@app.route('/insert', methods=["POST"])
def insert():

    user = {
        "matricula": request.form['matricula'],
        "nombre": request.form['nombre'],
        "correo": request.form['correo'],
        "contrasena": request.form['contrasena']
    }
    try:
        cuentas.insert_one(user)
        return redirect(url_for('find_all'))

    except Exception as e:
        return '<p>Unexpected error: %s %s </p>' % type(e), e


@app.route('/update', methods=['POST'])
def update():

    try:
        filter = {"matricula": request.form['matricula']}
        user = {"$set": {
            "nombre": request.form['nombre'], "correo": request.form['correo'], "contrasena": request.form['contrasena']}}
        cuentas.update_one(filter, user)
        return redirect(url_for('find_all'))

    except Exception as e:
        return '<p>Unexpected error: %s %s </p>' % type(e), e


@app.route('/find_one/<matricula>')
def find_one(matricula):
    cursor = cuentas.find_one({"id": (matricula)})
    return '<b>find : %s!</b>' % (cursor)


@app.route('/delete/<matricula>')
def delete(matricula):
    cursor = cuentas.delete_one({'matricula': (matricula)})
    if cursor.deleted_count == 0:
        return '<b>El registro no esta...!!</b>'
    else:
        return redirect(url_for('find_all'))


@app.route('/find_all')
def find_all():
    cursor = cuentas.find({})
    user = []
    for doc in cursor:
        user.append(doc)

    return render_template("/Retrieve.html", data=user)
    # return '<b>Nombre: %s!</b>' % (user.nombre)


if __name__ == '__main__':
    app.run(debug=True)
