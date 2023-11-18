#!/usr/bin/python3
"""
Creates an instance Base of declarative_base
Creates a class State that inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    Inherits from Base class
    links to the MySql table states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False,
                unique=True
                )
    name = Column(String(length=128), nullable=False)
