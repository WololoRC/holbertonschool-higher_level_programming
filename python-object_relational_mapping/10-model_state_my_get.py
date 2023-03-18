#!/usr/bin/python3
"""
Lists a record.id by input query
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    if len(argv[4]) >= 11:
        quit()

    record = session.query(State).filter(
            State.name == f"{argv[4]}").one_or_none()
    if record is None:
        print("Not found")

    else:
        print(f"{record.id}")
