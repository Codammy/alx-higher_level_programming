#!/usr/bin/python3
"""
creates the State California with the City 
San Francisco from the database hbtn_0e_100_usa
"""

if __name__ == '__main__':
    from relationship_city import City
    from relationship_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    user, key, db = sys.argv[1:]
    engine = create_engine(f'mysql+mysqldb://{user}:{key}@localhost:3306/{db}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    new_state = State()
    new_state.name = 'California'
    # new_state.cities.append('San Francisco')

    session.add(new_state)
    session.commit()
    new_city = City()
    new_city.name = 'San Francisco'
    new_city.state_id = new_state.id

    session.add(new_city)

    session.commit()
    session.close()
