import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#create flask app
app = Flask(__name__)

#mongo connection
app.config["MONGO_DBNAME"]= os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"]= os.getenv('MONGO_URI')

#creates pymongo
mongo = PyMongo(app)

#home route
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", definitions=mongo.db.Definitions.find().sort([("domain_name",1),("term",1)]))

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/add')
def add():
    return render_template("add.html", domains=mongo.db.Domains.find().sort("domain_name",1))

@app.route('/insert',methods=["POST"])
def insert():
    definitions= mongo.db.Definitions
    definitions.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

@app.route('/update/<definitionid>', methods=['POST'])
def update(definitionid):
    definitions= mongo.db.Definitions
    definitions.update({'_id':ObjectId(definitionid)},
    {
        'domain_name': request.form.get('domain_name'),
        'term': request.form.get('term'),
        'definition': request.form.get('definition')
    })
    return redirect(url_for('home'))

@app.route('/edit/<definitionid>')
def edit(definitionid):
    definition=mongo.db.Definitions.find_one({'_id':ObjectId(definitionid)})
    allcategories=mongo.db.Domains.find()
    return render_template('edit.html',definition=definition,domains=allcategories)

@app.route('/delete/<definitionid>')
def delete(definitionid):
    mongo.db.Definitions.remove({'_id':ObjectId(definitionid)})
    return redirect(url_for('home'))

@app.route('/domains')
def domains():
    return render_template('domains.html',domains=mongo.db.Domains.find().sort("domain_name",1))

@app.route('/edit_domain/<domainid>')
def edit_domain(domainid):
    return render_template('editdomain.html', domain=mongo.db.Domains.find_one({'_id':ObjectId(domainid)}))

@app.route('/update_domain/<domainid>',methods=['POST'])
def update_domain(domainid):
    mongo.db.Domains.update(
        {'_id':ObjectId(domainid)},
        {'domain_name':request.form.get('domain_name')})
    return redirect(url_for('domains'))    

@app.route('/delete_domain/<domainid>')
def delete_domain(domainid):
    mongo.db.Domains.remove({'_id':ObjectId(domainid)})
    return redirect(url_for('domains'))

@app.route('/insert_domain', methods=['POST'])
def insert_domain():
    domain=mongo.db.Domains
    domain_doc={'domain_name':request.form.get('domain_name')}
    domain.insert_one(domain_doc)
    return redirect(url_for('domains'))

@app.route('/add_domain')
def add_domain():
    return render_template('adddomain.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=False)

