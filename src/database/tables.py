import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv("DATABASE_URL"), convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class TodosTable(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    description = Column(Text)
    time = Column(DateTime)


class UsersTable(Base):
    __tablename__ = "users"

    id = Column(String, primary_key = True)
    email = Column(String)
    pass_hash = Column(String)
    premium = Column(Boolean)