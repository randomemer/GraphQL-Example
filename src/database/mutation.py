import graphene
from database.tables import db_session, TodosTable
from database.models import Todos, AddTodosFields

class AddTodo(graphene.Mutation):
    todo = graphene.Field(lambda: Todos)
    status = graphene.Boolean()

    class Arguments:
        input = AddTodosFields(required = True)

    @staticmethod
    def mutate(self, info, input):
        todo = TodosTable(**input)
        db_session.add(todo)
        db_session.commit()
        status = True
        return AddTodo(todo = todo, status = status)
    
class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(lambda: Todos)
    status = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)
        input = AddTodosFields(required=True)

    @staticmethod
    def mutate(self, info, id, input):
        todo = db_session.query(TodosTable).filter_by(id=id).first()
        if todo:
            for field, value in input.items():
                setattr(todo, field, value)
            db_session.commit()
            status = True
        else:
            status = False
        return UpdateTodo(todo=todo, status=status)

class DeleteTodo(graphene.Mutation):
    id = graphene.Int()
    status = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    @staticmethod
    def mutate(self, info, id):
        todo = db_session.query(TodosTable).filter_by(id=id).first()
        if todo:
            db_session.delete(todo)
            db_session.commit()
            status = True
        else:
            status = False
        return DeleteTodo(id=id, status=status)
    

class Mutation(graphene.ObjectType):
    addTodo = AddTodo.Field()
    updateTodo = UpdateTodo.Field()
    deleteTodo = DeleteTodo.Field()