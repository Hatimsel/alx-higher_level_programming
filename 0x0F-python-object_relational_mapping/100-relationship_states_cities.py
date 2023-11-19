#!/usr/bin/python3
"""
A script that creates the State California with the City
San Francisco from the database hbtn_0e_14_usa
"""
import sqlalchemy
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Script should take 3 arguments")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(sys.argv[1], sys.argv[2],
                                      sys.argv[3]), pool_pre_ping=True
                               )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        new_row = City(name='San Francisco', state=State(name='California'))
        session.add(new_row)
        session.commit()
