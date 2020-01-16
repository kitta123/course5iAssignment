from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource # new

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Price(db.Model):
    ListPrice = db.Column(db.String(20), primary_key=True)
    DollarsOff = db.Column(db.String(20))
    NetPrice = db.Column(db.String(20))
    Off = db.Column(db.String(20))
    HarmonyCost = db.Column(db.String(20))
    CostConcession = db.Column(db.String(20))
    SpecialCost = db.Column(db.String(20))
    Comments = db.Column(db.String(20))

    def __init__(self, ListPrice, DollarsOff, NetPrice,Off,HarmonyCost,CostConcession,SpecialCost,Comments):
        self.ListPrice = ListPrice
        self.DollarsOff = DollarsOff
        self.NetPrice = NetPrice
        self.Off = Off
        self.HarmonyCost = HarmonyCost
        self.CostConcession = CostConcession
        self.SpecialCost = SpecialCost
        self.Comments = Comments

@app.route('/pricelist/', methods = ['GET'])
def index():
    return jsonify({'price list': Price.query.all()})

@app.route('/pricelist/<int:id>/')
def get_dev(id):
    return jsonify({'price list': Price.query.get(id)})

@app.route('/pricelist/', methods = ['POST'])
def create_price():
    if not request.json or not 'ListPrice' in request.json:
        abort(400)
    pricedata = Price(request.json.get('ListPrice',''), request.json.get('DollarsOff', ''),
    request.json.get('NetPrice',''), request.json.get('Off', ''),
    request.json.get('HarmonyCost',''), request.json.get('CostConcession', ''),
    request.json.get('SpecialCost',''), request.json.get('Comments', ''))
    db.session.add(pricedata)
    db.session.commit()
    return jsonify( { 'price list': pricedata } ), 201

# @app.route('/dev/<int:id>', methods = ['DELETE'])
# def delete_dev(id):
#     db.session.delete(Users.query.get(id))
#     db.session.commit()
#     return jsonify( { 'result': True } )

# @app.route('/dev/<int:id>', methods = ['PUT'])
# def update_dev(id):
#     dev = Developer.query.get(id)
#     dev.name = request.json.get('name', dev.name)
#     dev.hireDate = request.json.get('hireDate',dev.name)
#     dev.focus = request.json.get('focus', dev.focus)
#     db.session.commit()
#     return jsonify( { 'dev': dev } )

if __name__ == '__main__':
    app.run(debug=True)
