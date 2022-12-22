#imports
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import  declarative_base
from  sqlalchemy.orm import sessionmaker

# url
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"

# create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# create engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base
Base = declarative_base()

