#!/usr/bin/python3
"""
Python script that lists all State objs that contains
the letter a from a db
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State)\
            .filter(State.name.like('%a%'))\
            .order_by(asc(State.id)).all():
        print("{}: {}".format(row.id, row.name))
