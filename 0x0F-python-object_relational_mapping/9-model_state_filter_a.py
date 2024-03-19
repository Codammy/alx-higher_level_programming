#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_state import (Base, State)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.ilike('%a%')).\
        order_by(State.id)
    for d in data:
        print(f'{d.id}: {d.name}')
    session.close()
