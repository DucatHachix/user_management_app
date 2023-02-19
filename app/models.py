from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))  
    addr = db.Column(db.String(200))

    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    
    def __repr__(self):
        return '%s/%s/%s/%s' % (self.id, self.name, self.email, self.addr)