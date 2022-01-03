from fastapi import FastAPI
from dotenv import dotenv_values
import os
from routes import Authentication
from database import SessionLocal , engine
from models import User

config = dotenv_values(".env")
User.Base.metadata.create_all(bind=engine)

app = FastAPI( docs_url='/api-docs')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(Authentication.router , prefix='/api/auth' , tags=['Authentication'])

