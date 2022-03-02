import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    person_firstname = Column(String(250), nullable=False)
    person_lastname = Column(String(250), nullable=False)
    password = Column(String(20),nullable=False)
    email = Column(String(50),unique=True)
    

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable = False)
    homeworld = Column(String(50), ForeignKey('planet.name'))

class Planet(Base):
    __tablename__ = 'planet' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter=Column(Integer)
    population=Column(Integer)
    climate=Column(String(50))
    relationvehicle = relationship("Vehicle")
    relationcharacter = relationship("Character")

class Vehicle(Base):
    __tablename__ = 'vehicle' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model= Column(String(50))
    vehicle_class=Column(String(50))
    length=Column(Integer)
    manufacturer = Column(String(50), ForeignKey('planet.name'))
    pilot_uid= Column(Integer,ForeignKey('character.uid'))
    relationcharacter= relationship("Character")

class Favourite_list(Base):  
   __tablename__ = 'favourite_list'
   id = Column(Integer, primary_key=True)
   user_id=Column(Integer,ForeignKey('user.id'))
   favourite_character=Column(Integer,ForeignKey('character.uid'))
   favourite_planet=Column(Integer, ForeignKey('planet.id'))
   favourite_vehicle=Column(Integer, ForeignKey('vehicle.id'))
   relationuser = relationship("User")
   relationcharacter= relationship("Character")
   relationplanet= relationship("Planet")
   relationvehicle= relationship("Vehicle")


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')