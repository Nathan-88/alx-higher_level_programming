#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    dbsession = Session()
    result = dbsession.query(State, City).join(City, State.id ==
                                               City.state_id).order_by(
                                                   City.id.asc()).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    dbsession.close()
