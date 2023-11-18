#!/usr/bin/python3
"""
Creates an instance Base of declarative_base
Creates a class City that inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class City(Base):
    """
    Inherits from Base class
    links to the MySql table cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False,
                unique=True
                )
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
