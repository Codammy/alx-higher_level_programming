#!/usr/bin/python3
"""
contains the class definition of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column
of an auto-generated, unique integer, can’t be nulland is a primary key
class attribute name that represents a column of a string of 128 characters
and can’t be null
class attribute state_id that represents a column of an integer,
can’t be null and is a foreign key to states.id
"""


if __name__ == "__main__":
    from model_state import Base
    from sqlalchemy import (Column, Integer, String, ForeignKey)
    class City(Base):
        """class documented"""
        __tablename__ = "cities"
        id = Column(Integer, primary_key, nullable=False, unique=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
        