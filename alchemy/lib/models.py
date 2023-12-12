from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Sneaker(Base):
    __tablename__ = "sneakers"
    
    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    colour = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    is_available = Column(Boolean, nullable=False)
    
    reviews_sneaker = relationship("Review", back_populates = "sneaker")
    
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(Integer, nullable=False)
    
    reviews_customer = relationship("Review", back_populates = "customer")

    
class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    sneaker_id = Column(Integer, ForeignKey("sneakers.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    
    sneaker = relationship("Sneaker", back_populates = "reviews_sneaker")
    customer = relationship("Customer", back_populates = "reviews_customer")