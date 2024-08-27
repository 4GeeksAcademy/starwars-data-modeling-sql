import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()




class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False)
    favoritos = relationship("Favorito", backref="usuario", lazy=True)


class Personaje(Base):
    __tablename__ = "personaje"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    especie_id = Column(Integer, ForeignKey("especie.id"), nullable=False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"), nullable=False)
    favoritos = relationship("Favorito", backref="personaje", lazy=True)

class Planeta(Base):
    __tablename__="planeta"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    clima = Column(String(100), nullable=False)
    personajes = relationship("Personaje", backref="planeta", lazy=True)
    favoritos = relationship("Favorito", backref="planeta", lazy=True)

class Especie(Base):
    __tablename__="especie"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"), nullable=False)
    personajes = relationship("Personaje", backref="especie", lazy=True)
    favoritos = relationship("Favorito", backref="especie", lazy=True)


class Favorito(Base):
    __tablename__= "favorito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable = False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"), nullable = False)
    especie_id = Column(Integer, ForeignKey("especie.id"), nullable = False)
    personaje_id = Column(Integer, ForeignKey("personaje.id"), nullable = False)
 
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
