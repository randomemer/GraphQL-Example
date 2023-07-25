from modules.core import app, db, UsersTable
from flask import request, make_response, render_template, jsonify
from werkzeug.security import generate_password_hash
import uuid


@app.get("/register")
def register_get():
    return render_template("register.html")

@app.post("/register")
def register_post():
    data = request.form
    email, password = data.get("email"), data.get("password")

    exists = UsersTable.query.filter_by(email = email).first()

    if not exists:
        user = UsersTable(
            id = uuid.uuid4(),
            email = email,
            pass_hash = generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        return make_response(jsonify({ "messsage": "Registered" }), 201)
    else:
        return make_response('User already exists. Please Log in.', 202)
