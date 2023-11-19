#!/usr/bin/python3
"""
A script that lists all City objects
from the database hbtn_0e_101_usa
"""
import sqlalchemy
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

        for c in session.query(City).all():
            print("{}: {} -> {}".format(c.id, c.name, c.state.name))
        session.close()
