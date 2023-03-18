#!/usr/bin/python3
""" Create a Session instance and made and list by states.id=1 query
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

    record = session.query(State).filter(State.id == 1).one_or_none()

    if record is None:
        print('Nothing')

    else:
        print(f"{record.id}: {record.name}")
