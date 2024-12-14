import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.config import DATABASE_URL, TEST_DATABASE_URL

engine = create_engine(TEST_DATABASE_URL if "pytest" in os.getenv("PYTHON_ENV", "") else DATABASE_URL)
Session = sessionmaker(bind=engine)


class DatabaseManager:
    def __init__(self):
        self.session = Session()

    def close(self):
        self.session.close()
