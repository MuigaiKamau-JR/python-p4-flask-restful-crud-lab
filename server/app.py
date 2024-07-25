#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class PlantByID(Resource):

    def patch(self, id):
        record = Plant.query.filter_by(id=id).first()
        if not record:
            return make_response({"error": "Plant not found"}, 404)

        data = request.get_json()
        for attr in data:
            setattr(record, attr, data[attr])

        db.session.add(record)
        db.session.commit()

        response_dict = record.to_dict()

        response = make_response(
            response_dict,
            200
        )
        return response

    def delete(self, id):
        record = Plant.query.filter_by(id=id).first()
        if not record:
            return make_response({"error": "Plant not found"}, 404)

        db.session.delete(record)
        db.session.commit()

        response = make_response("", 204)
        return response

api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
