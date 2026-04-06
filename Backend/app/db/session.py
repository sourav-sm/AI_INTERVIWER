from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import database_url


engine = create_engine(database_url, echo=True)


SessionLocal= sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()