#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import (Base, State)

    nm, key, db, searched= sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(nm, key, db))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    data = session.query(State).filter(State.name == searched)\
                         .order_by(State.id).first()
    print(f'{data.id if data else "Not found"}')
