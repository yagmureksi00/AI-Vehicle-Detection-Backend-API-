import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Database URL
# Get Database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")


if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DB_URL not found! Please check your .env file.")

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models
Base = declarative_base()

# Optional: Connection Test (Can be removed in production)
try:
    with engine.connect() as connection:
        print("✅ Connection Successful! Database is accessible.")
except Exception as e:
    print(f"❌ An error occurred: {e}")




try:
    with engine.connect() as connection:
        print("✅ Connection Successful! Database is accessible.")
except Exception as e:
    print(f"❌ An error occurred: {e}")