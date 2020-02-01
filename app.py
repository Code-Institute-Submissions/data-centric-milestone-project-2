import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"]= os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"]= os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/testroute')
def test():
    return render_template("index.html", definicoes=mongo.db.Definitions.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP',"0.0.0.0"),
    port=os.environ.get('PORT',"5000"),
    debug=True)

