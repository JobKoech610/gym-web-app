from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Admin, User, Profile, Category, Payment, User_category


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


migrate = Migrate(app,db)

db.init_app(app)
api = Api(app)
class Index(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome",
        }

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response

api.add_resource(Index, '/')

class Admins(Resource):
    def get(self):
        response_dict_list = [A.to_dict() for A in Admin.query.all()]
        response = make_response(
            jsonify(response_dict_list),
            200,
        )
        return response

    def post(self):
        new_admin = Admin(
            admin_id = request.form['admin_id'],
            phone_number = request.form['phone_number'],
            name = request.form['name'],
        )    

        db.session.add(new_admin)
        db.session.commit()

        response_dict = new_admin.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )
        return response
api.add_resource(Admins, '/admins')        



    


if __name__ == "__main__":
    app.run(port="5555", debug=True) 