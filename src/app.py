"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario, Planetas, Personajes
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/people', methods=['GET'])
def get_people():
    people = Personajes.query.all()
    people = list(map(lambda x: x.serialize(), people))
    if not people:
        raise APIException("User not found", status_code=404)

    return jsonify(people), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_people_id(id):
    people = Personajes.query.get(id)
    if not people:
        return jsonify({"error": "User not found"}), 404
    return jsonify(people.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_planetas():
    planets = Planetas.query.all()
    planets = list(map(lambda x: x.serialize(), planets))
    if not planets:
        raise APIException("User not found", status_code=404)

    return jsonify(planets), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_planetas_id(id):
    planets = Planetas.query.get(id)
    if not planets:
        return jsonify({"error": "User not found"}), 404
    return jsonify(planets.serialize()), 200

@app.route('/usuario', methods=['GET'])
def get_usuario():
    usuario = Usuario.query.all()
    usuario = list(map(lambda x: x.serialize(), usuario))
    if not usuario:
        raise APIException("User not found", status_code=404)

    return jsonify(usuario), 200

@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_id(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "User not found"}), 404
    return jsonify(usuario.serialize()), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
