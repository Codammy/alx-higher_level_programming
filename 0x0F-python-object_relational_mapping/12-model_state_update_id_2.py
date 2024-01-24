#!/usr/bin/python3
"""
script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    usr, key, db = sys.argv[1:]
    engine = create_engine(f"mysql+mysqldb://{usr}:{key}@localhost/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id==2).update({State.name: "New Mexico"})
    session.commit()
