import graphene
from graph_ql.query import Query
from models import Todos


schema = graphene.Schema(
    query=Query, types=[Todos]
)