from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(30), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    salt = Column(String(32), nullable=False)

    created_at = Column(DateTime, default=datetime.now())