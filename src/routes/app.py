from flask import request, render_template
from modules.core import app 
from modules.auth import private_route

@app.get("/app")
@private_route
def app_route(cur_user):
    return render_template("app.html")