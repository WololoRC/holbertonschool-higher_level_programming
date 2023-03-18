#!/usr/bin/python3
"""
Join and lists all records on City and State
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for a, b in session.query(
            State, City).filter(State.id == City.state_id).all():

        print(f"{a.name}: ({b.id}) {b.name}")
