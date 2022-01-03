from sqlalchemy import Column  , Integer , String , TEXT
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , autoincrement=True, nullable=False , primary_key=True)
    email = Column(String(255) , nullable=False , unique=True )
    username=Column(String(255) , nullable=False , unique=True)
    password=Column(String(255) , nullable=False )
