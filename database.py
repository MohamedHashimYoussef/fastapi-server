from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values
config = dotenv_values('.env')
DB_USER = config['DB_USER']
DB_PASSWORD = config['DB_PASSWORD']
DB_NAME = config['DB_NAME']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1/{DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()