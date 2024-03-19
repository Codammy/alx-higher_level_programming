#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys;
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    state = State()
    state.name = 'Louisiana'
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(*sys.argv[1:]))
    session = sessionmaker(bind=engine)()
    session.add(state)
    session.commit()
    print(state.id)
    session.close()

