#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user, key, db = sys.argv[1:]

    engine = create_engine(f'mysql+mysqldb://{user}:{key}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    results = session.query(State, City).join(City)
    for r in results.order_by(City.id):
        state, city = r
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
