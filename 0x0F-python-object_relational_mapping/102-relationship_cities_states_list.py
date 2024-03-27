#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
