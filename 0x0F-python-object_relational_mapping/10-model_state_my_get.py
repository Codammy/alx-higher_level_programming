#!/usr/bin/python3
"""
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    usr, key, db, name = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usr, key, db))
    Session = sessionmaker(bind=engine)
    i = 0
    for state in Session().query(State).\
            order_by(State.id).filter(State.name==name):
                i = 1
                print(f"{state.id}")
    if i != 1:
        print("Not found")
