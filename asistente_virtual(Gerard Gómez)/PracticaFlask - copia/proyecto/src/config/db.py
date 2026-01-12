from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()