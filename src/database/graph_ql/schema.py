import graphene
from database.graph_ql.query import Query
from database.graph_ql.models import Todos
from database.graph_ql.mutation import Mutation

schema = graphene.Schema(
    query=Query, 
    mutation=Mutation,
    types=[Todos]
)