#!/usr/bin/python3
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    a class that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)
