from config import *
from sqlalchemy.orm import sessionmaker
from models import Sneaker, Customer, Review

# CRUD OPERATIONS FOR THE USER/CUSTOMER

def get_user_details(session, user_id):
    """Retrieve details about a customer using their ID"""
    user = session.query(Customer).filter_by(id=user_id).first()
    return user

def delete_customer(session, customer_id):
    """Delete a customer by providing their ID"""
    customer = session.query(Customer).filter_by(id=customer_id).first()
    session.delete(customer)
    session.commit()


# CRUD OPERATIONS FOR THE SNEAKER

def get_sneaker_details(session, sneaker_id):
    """Retrieve details about a sneaker using its ID"""
    sneaker = session.query(Sneaker).filter_by(id=sneaker_id).first()
    return sneaker

def get_unavailable_sneakers(session):
    """Fetch all the unavailable sneakers for re-stock"""
    unavailable_sneakers = session.query(Sneaker).filter_by(is_available=False).all()
    return unavailable_sneakers

def remove_sneaker(session, sneaker_id):
    """Remove a sneaker by providing its ID"""
    sneaker = session.query(Sneaker).filter_by(id=sneaker_id).first()
    session.delete(sneaker)
    session.commit()


# CRUD OPERATIONS FOR REVIEWS

def get_reviews_for_sneaker(session, sneaker_id):
    """Fetch all the reviews associated with a particular sneaker"""
    reviews = session.query(Review).filter_by(sneaker_id=sneaker_id).all()
    return reviews

def get_reviews_for_user(session, user_id):
    """Fetch all the reviews associated with a particular user"""
    reviews = session.query(Review).filter_by(customer_id=user_id).all()
    return reviews