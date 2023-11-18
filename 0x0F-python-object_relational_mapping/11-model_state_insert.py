#!/usr/bin/python3
"""
A script that adds the State object 'Louisiana'
to the database hbtn_0e_6_usa
"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
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
        Session = sessionmaker(bind=engine)
        session = Session()
        new_row = State(name="Louisiana")
        session.add(new_row)
        session.commit()
        print(new_row.id)
