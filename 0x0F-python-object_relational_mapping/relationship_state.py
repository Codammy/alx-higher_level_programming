#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base():
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()


class State(Base):
    """State Class for State model"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(128))
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
