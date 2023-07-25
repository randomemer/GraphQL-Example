import datetime
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.tables import TodosTable

class Todos(SQLAlchemyObjectType):
    class Meta:
        model = TodosTable


class TodosFields:
    id = graphene.Int()
    title = graphene.String(required = True)
    description = graphene.String(required = True)
    time = graphene.DateTime()


class AddTodosFields(graphene.InputObjectType, TodosFields):
    pass