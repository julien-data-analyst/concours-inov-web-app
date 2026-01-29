from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Engin creation to connect to PostgreSQL Database
engine = create_engine(
    os.getenv("DB_URL"),
    echo=True,
    pool_pre_ping=True)

# Session creation
SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)

# Base creation
Base = declarative_base()