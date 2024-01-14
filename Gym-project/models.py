
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Admin(db.Model, SerializerMixin):
    __tablename__='admins'

    id = db.Column(db.Integer, primary_key=True)
    admin_id= db.Column(db.Integer, unique=True)
    name= db.Column(db.String, nullable=False)
    phone_number= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Admin {self.name}.>'



class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String, nullable=False)
    last_name= db.Column(db.String, nullable=False)
    email= db.Column(db.String, unique=True)
    password= db.Column(db.String, unique=True)
    phone_number= db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Profile(db.Model):
    __tablename__='profiles'

    id = db.Column(db.Integer, primary_key=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    place_of_work = db.Column(db.String(255))
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    body_mass_index = db.Column(db.Float, nullable=False)
    body_fat = db.Column(db.Float, nullable=False)
    v_fat = db.Column(db.Float, nullable=False)
    kilo_calories = db.Column(db.Float, nullable=False)
    


class Category(db.Model):
    __tablename__='categories' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, unique=True)




class Payment(db.Model):
    __tablename__='payments'

    id = db.Column(db.Integer, primary_key=True)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



class User_category(db.Model):
    __tablename__='usercategories' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)




    