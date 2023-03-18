#!/usr/bin/python3
"""
Create a Session instance and made a SELECT * query
filltering by name where like %a%
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

    records = (
            session.query(State).order_by(
                State.id).filter(State.name.like('%a%')).all())

    for record in records:
        print(f"{record.id}: {record.name}")
