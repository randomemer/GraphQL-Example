import os
from keycloak import KeycloakOpenID

keycloak_client = KeycloakOpenID(
    server_url= os.getenv("KC_URL"),
    realm_name= os.getenv("KC_REALM"),
    client_id= os.getenv("KC_CLIENT"),
    client_secret_key= os.getenv("KC_CLIENT_SECRET")
)

sessions = dict()