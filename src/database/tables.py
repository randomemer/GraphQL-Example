import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
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