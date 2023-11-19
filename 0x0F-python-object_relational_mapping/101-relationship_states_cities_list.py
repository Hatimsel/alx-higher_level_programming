#!/usr/bin/python3
"""
A script that all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
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

        for s in session.query(State).order_by(s.id).all():
            print("{}: {}".format(s.id, s.name))
            for c in s.cities:
                print("\t{}: {}".format(c.id, c.name))
        session.close()
