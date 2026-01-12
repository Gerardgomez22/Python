from sqlalchemy import Column, Integer, String, Float
from src.config.db import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    price = Column(Float)