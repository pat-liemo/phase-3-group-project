from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from models import Base, Sneaker, Customer, Review

# Set up SQLite database engine
engine = create_engine("sqlite:///database.sqlite")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()