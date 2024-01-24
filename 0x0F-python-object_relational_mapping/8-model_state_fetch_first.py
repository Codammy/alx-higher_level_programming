#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa   
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import State, Base

    usr, key, db = sys.argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(usr, key, db))
    Session = sessionmaker(bind=engine)
    state = Session().query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
