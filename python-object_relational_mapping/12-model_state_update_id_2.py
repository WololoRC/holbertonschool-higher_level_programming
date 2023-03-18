#!/usr/bin/python3
"""
Update record.name where record.id == 2
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).filter(State.id == 2).one()
    record.name = 'New Mexico'
    session.commit()
