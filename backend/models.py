from sqlalchemy import Column, BIGINT, VARCHAR, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(BIGINT, primary_key=True, index=True)
    login = Column(VARCHAR, unique=True)
    password = Column(VARCHAR)

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(VARCHAR)
    description = Column(VARCHAR)
    difficulty = Column(Integer)