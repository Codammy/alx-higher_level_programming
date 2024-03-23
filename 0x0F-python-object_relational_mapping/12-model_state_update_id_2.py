#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(*sys.argv[1:]))
    session = sessionmaker(bind=engine)()
    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()
