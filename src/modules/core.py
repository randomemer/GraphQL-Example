import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.tables import db_session
from database.schema import schema



app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create tables

db = SQLAlchemy(app)

class UsersTable(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    pass_hash = db.Column(db.String(255), nullable=False)
    premium = db.Column(db.Boolean, nullable=False, default=False)
    

class TodosTable(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    user_id = db.Column(db.String(255), db.ForeignKey(UsersTable.id), nullable = False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=True, onupdate=db.func.current_timestamp())


with app.app_context():
    db.create_all()
    db.session.commit()