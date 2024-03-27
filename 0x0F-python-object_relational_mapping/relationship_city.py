#!/usr/bin/python3
"""contains the class definition of a City."""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """city class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement='auto',
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
