#!/usr/bin/python3
"""
Python script that lists all City objs from a db
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for s, c in session.query(State, City)\
            .filter(State.id == City.state_id)\
            .order_by(asc(City.id)).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
