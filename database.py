import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

if not SQLALCHEMY_DATABASE_URL:

    print("⚠️ UYARI: DB_URL bulunamadı. Veritabanı bağlantısı yapılamayabilir.")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" 

if SQLALCHEMY_DATABASE_URL.startswith("mysql://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

# Create the database engine

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600)
except Exception as e:
    print(f"❌ Motor Oluşturma Hatası: {e}")
    raise e

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models
Base = declarative_base()

# Connection Test
try:
    with engine.connect() as connection:
        print("✅ Connection Successful! Database is accessible.")
except Exception as e:
    print(f"❌ Connection Failed: {e}")