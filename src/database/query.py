import graphene
from database.tables import TodosTable
from database.models import Todos

class Query(graphene.ObjectType):
    get_todos = graphene.List(Todos)
    
    @staticmethod
    def resolve_get_todos(parent, info, **kwargs):
        return Todos.get_query(info).all()