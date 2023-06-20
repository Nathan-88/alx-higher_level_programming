#!/usr/bin/python3
"""
a python file that contains the class definition of a City and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    a class that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto", unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
