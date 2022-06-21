from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql+psycopg2://messenger:1234567@localhost:5432/messengerpy'
engine = create_engine(db_url)
session = sessionmaker(engine)