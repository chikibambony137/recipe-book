from sqlalchemy import Column, BIGINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(BIGINT, primary_key=True, index=True)
    login = Column(VARCHAR, unique=True)
    password = Column(VARCHAR)