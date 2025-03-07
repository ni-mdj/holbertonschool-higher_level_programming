#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()