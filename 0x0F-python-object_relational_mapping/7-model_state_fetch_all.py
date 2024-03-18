#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import (State, Base)

    uname, key, db = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(uname, key, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    data = session.query(State).order_by(State.id)
    print(data)
    for d in data:
        print(f'{d.id}: {d.name}')
