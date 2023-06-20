#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    dbsession = Session()
    result = dbsession.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))
    dbsession.close()
