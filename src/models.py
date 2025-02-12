import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table users
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    favs_planets: Mapped["Favs_planets"] = relationship(back_populates="users")
    favs_characters: Mapped["Favs_characters"] = relationship(back_populates="users")

class Characters_planets(Base):
    __tablename__ = 'characters_planets'
    # Here we define columns for the table characters & planets
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    favs_planets: Mapped["Favs_planets"] = relationship(back_populates="characters_planets")
    favs_planets: Mapped["Favs_characters"] = relationship(back_populates="characters_planets")

class Favs_planets(Base):
    __tablename__ = 'favs_planets'
    # Here we define columns for the table favs_planets.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["Users"] = relationship(back_populates="favs_planets")
    charaters_planets_id: Mapped[int] = mapped_column(ForeignKey("characters_planets.id"))
    characters_planets: Mapped["Characters_planets"] = relationship(back_populates="favs_planets")

class Favs_characters(Base):
    __tablename__ = 'favs_characters'
    # Here we define columns for the table favs_characters.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["Users"] = relationship(back_populates="favs_characters")
    charaters_planets_id: Mapped[int] = mapped_column(ForeignKey("characters_planets.id"))
    characters_planets: Mapped["Characters_planets"] = relationship(back_populates="favs_characters")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
