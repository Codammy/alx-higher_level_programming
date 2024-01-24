#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    usr, key, db = argv[1:]
    engine = create_engine(f"mysql+mysqldb://{usr}:{key}@localhost/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    for session.query

