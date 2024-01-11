#!/usr/bin/python3
"""
Python script that the State obj with the name
passed as argument from a db
"""
import sys
from model_state import Base, State
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

    state_name = sys.argv[4]
    row = session.query(State)\
        .filter(State.name == (state_name,)).first()
    if (row):
        print("{}".format(row.id))
    else:
        print("Not found")
