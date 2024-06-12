from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = 'sqlite:///blogmaster.db'

engine = create_engine(DATABASE_URL,  echo=True)
Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(bind=engine)
