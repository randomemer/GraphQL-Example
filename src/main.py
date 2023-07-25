from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, make_response
from database.tables import db_session
from database.schema import schema
from kc import keycloak_client, sessions

app = Flask(__name__)
app.debug = True

@app.get("/")
def index():
    redirect_uri = f"{request.url_root}callback"
    auth_url = keycloak_client.auth_url(
        redirect_uri=redirect_uri, 
        scope="email"
    )

    return render_template(
        "index.html",
        auth_url = auth_url
    )


@app.get("/callback")
def callback():
    code = request.args.get("code")
    # Exchange for token
    if code:
        token = keycloak_client.token(
            grant_type="authorization_code",
            redirect_uri=f"{request.url_root}callback",
            code=code
        )

        session_state = token.get("session_state")
        sessions[session_state] = token.get("access_token")

        resp = make_response(redirect(url_for("app_route")))
        resp.set_cookie("kc_session", session_state)

        return resp
    else:
        return "Something went wrong."
    
    
@app.get("/app")
def app_route():
    session_id = request.cookies.get("kc_session")
    token = sessions.get(session_id)

    print("token in app :", token)

    user = keycloak_client.userinfo(token=token)
    print(user)

    return render_template("app.html")
        

if __name__ == "__main__":
    app.run(port=4000)