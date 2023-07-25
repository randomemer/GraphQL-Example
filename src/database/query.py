import graphene
from database.tables import TodosTable, UsersTable
from database.models import Todos, Users

class Query(graphene.ObjectType):
    get_todos_by_email = graphene.List(Todos)
    get_user_by_email = graphene.Field(Users, email = graphene.String())
    
    @staticmethod
    def resolve_get_todos(parent, info, **kwargs):
        return Todos.get_query(info).filter(TodosTable).all()

    @staticmethod
    def resolve_get_user_by_email(parent, info, **kwargs):
        email = kwargs.get("email")
        return Users.get_query(info).filter(UsersTable.email.contains(email)).first()