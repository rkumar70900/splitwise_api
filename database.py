from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password = "2aoySvGG=18!s9oNE}PB"
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/splitwise_api")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()