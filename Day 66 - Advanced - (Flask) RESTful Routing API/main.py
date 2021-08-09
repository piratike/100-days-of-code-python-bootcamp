from flask import Flask, json, jsonify, render_template, request
from flask.wrappers import JSONMixin
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def as_dict(self):
        return {cafe.name: str(getattr(self, cafe.name)) for cafe in self.__table__.columns}


@app.route('/')
def home():
    return render_template('index.html')
    


@app.route('/random', methods=['GET'])
def get_random():
    random_cafe = Cafe.query.get(random.randint(1, len(Cafe.query.all())))
    return jsonify(cafe={
        'id': random_cafe.id,
        'name': random_cafe.name,
        'map_url': random_cafe.map_url,
        'img_url': random_cafe.img_url,
        'location': random_cafe.location,
        'seats': random_cafe.seats,
        'has_toilet': random_cafe.has_toilet,
        'has_wifi': random_cafe.has_wifi,
        'has_sockets': random_cafe.has_sockets,
        'can_take_calls': random_cafe.can_take_calls,
        'coffee_price': random_cafe.coffee_price
    })


## HTTP GET - Get Record/s
@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(cafes = [cafe.as_dict() for cafe in Cafe.query.all()])


@app.route('/search', methods=['GET'])
def search():
    cafes_list = [cafe.as_dict() for cafe in Cafe.query.filter(Cafe.location == request.args['loc'])]
    return jsonify(cafes=cafes_list) if cafes_list else jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe at that location.'})


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price'),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={'Success': 'Successfully added the new cafe.'})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_price(id):
    cafe_to_update = db.session.query(Cafe).get(id)

    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get('price')
        db.session.commit()

        return jsonify(response={'Success': 'Successfully updated the cafe.'})

    return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe at that location.'})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api-key")

    if api_key == "Secreto":
        cafe = db.session.query(Cafe).get(id)

        if cafe:
            db.session.delete(cafe)
            db.session.commit()

            return jsonify(response={"Success": "Successfully deleted the cafe from the database."}), 200

        else:

            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    else:

        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
