#!/usr/bin/python3
"""
Base class and State class

Base: A class for SQL mappin

State: Inherits from Base and his from record inside @states table

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
