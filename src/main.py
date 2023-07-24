from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from flask_graphql import GraphQLView as View
from database.graph_ql.tables import db_session
from database.graph_ql.schema import schema

app = Flask(__name__)
app.debug = True
app.add_url_rule("/", view_func= View.as_view("graphql", graphiql =True, schema = schema))
app.run()