#!/usr/bin/python3
"""
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    usr, key, db = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usr, key, db))
    Session = sessionmaker(bind=engine)

    for state in Session().query(State).\
            order_by(State.id).filter(State.name.like("%a%")):
        print(f"{state.id}: {state.name}")
