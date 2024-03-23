#!/usr/bin/python3
"""
deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(*sys.argv[1:]))
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.ilike("%a%"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
