import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"]= "DataCentricDB"
app.config["MONGO_URI"]= "mongodb+srv://root:r00tUser@myfirstcluster-ur23i.mongodb.net/DataCentricDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/testroute')
def test():
    return render_template("index.html", definicoes=mongo.db.Definitions.find())

@app.route('/add')
def add():
    return render_template("add.html", domains=mongo.db.Domains.find())

@app.route('/insert',methods=["POST"])
def insert():
    definitions= mongo.db.Definitions
    definitions.insert_one(request.form.to_dict())
    return redirect(url_for('test'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP',"0.0.0.0"),
    port=os.environ.get('PORT',"5000"),
    debug=True)

