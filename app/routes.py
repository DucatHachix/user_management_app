from app import app,db
from app.models import User
from flask import jsonify, request

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

@app.route('/user/<id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        body = request.json
        new_name = body['name']
        new_email = body['email']
        new_addr = body['addr']
        edit_data = User.query.filter_by(id=id).first()
        edit_data.name = new_name
        edit_data.email = new_email
        edit_data.addr = new_addr
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})
    

@app.route('/user/<id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        del_data = User.query.filter_by(id=id).first()
        db.session.delete(del_data)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})