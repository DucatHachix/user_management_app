# LAU LE - https://levanlau.net
import os
from flask import Flask, jsonify, request, json, make_response, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(    
    os.environ.get('DB_USER', 'app_user'),
    os.environ.get('DB_PASS', 'app_password'),
    os.environ.get('DB_HOST', 'app'),
    os.environ.get('DB_NAME', 'app_db')
)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))  
    addr = db.Column(db.String(200))

    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    
    def __repr__(self):
        return '%s/%s/%s/%s' % (self.id, self.name, self.email, self.addr)
        
@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    db.session.commit()

@app.route('/user', methods=['POST'])
def create():
    if request.method == 'POST':
        body = request.json
        name = body['name']
        email = body['email']
        addr = body['addr']

        data = User(name, email, addr)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!'
        })

@app.route('/user', methods=['GET'])
def read():
    if request.method == 'GET':
        
        data = User.query.order_by(User.id).all()
        dataJson = []
        for i in range(len(data)):
            print(str(data[i]).split('/'))
            dataDict = {
                'id': str(data[i]).split('/')[0],
                'name': str(data[i]).split('/')[1],
                'email': str(data[i]).split('/')[2],
                'addr': str(data[i]).split('/')[3]
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
        # return jsonify({
        #     'status': 'Data is retrieved!'
        # })

@app.route('/data/<id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        body = request.json
        newName = body['name']
        newEmail = body['email']
        newAddr = body['addr']
        editData = User.query.filter_by(id=id).first()
        editData.name = newName
        editData.email = newEmail
        editData.addr = newAddr
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})
    

@app.route('/data/<id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        delData = User.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
