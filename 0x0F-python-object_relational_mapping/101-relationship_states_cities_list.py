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

        for s, c in session.query(State, City)\
        .filter(s.id == c.state_id).order_by(s.id, c.id):
            print("{}: {}\n".format(s.id, s.name), end='')
            while (c.id):
                print("\t{}: {}".format(c.id, c.name))
                c.id++
