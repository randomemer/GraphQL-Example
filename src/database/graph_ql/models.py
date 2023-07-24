import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.tables.todos import TodosTable

class Todos(SQLAlchemyObjectType):
    class Meta:
        model = TodosTable


class TodosFields:
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    time = graphene.DateTime()


class AddTodosFields(graphene.InputObjectType, TodosFields):
    pass