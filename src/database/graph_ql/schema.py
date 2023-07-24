import graphene
from database.graph_ql.query import Query
from database.graph_ql.models import Todos


schema = graphene.Schema(
    query=Query, types=[Todos]
)