#!/usr/bin/python3
"""
a script that changes the name of a State object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
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
    result = dbsession.query(State).filter(State.id == 2).first()
    if result:
        result.name = "New Maxico"
        dbsession.commit()
    dbsession.close()
