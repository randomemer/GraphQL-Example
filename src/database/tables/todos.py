from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:Programmer#1@localhost:3306/todoapp", convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class TodosTable(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    description = Column(Text)
    time = Column(DateTime)