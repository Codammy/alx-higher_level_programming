#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import (State, Base)
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).order_by(State.id).first()
    if data is not None:
        print(f'{data.id}: {data.name}')
    else:
        print('Nothing')
    session.close()
