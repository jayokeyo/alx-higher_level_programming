#!/usr/bin/python3
'''
class definition of a State and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''
    class definition of a State
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    '''
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
