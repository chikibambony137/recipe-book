from sqlalchemy import create_engine, select, column
from sqlalchemy.orm import sessionmaker
import config

# postgresql://postgres:0053@db/recipe-list
DATABASE_URL = config.DB_URL
engine = create_engine(DATABASE_URL)

def get_db():
    SessionLocal = sessionmaker(autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()