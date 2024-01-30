#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    import sys

    usr, key, db = sys.argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usr, key, db))
    Session = sessionmaker(bind=engine)
    for state in Session().query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")