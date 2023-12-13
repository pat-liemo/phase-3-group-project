from config import *

def get_sneaker(sneaker_id):
    return session.query(Sneaker).get(sneaker_id)

def get_customer(customer_id):
    return session.query(Customer).get(customer_id)

def get_reviews(customer_id=None, sneaker_id=None):
    if customer_id:
        return session.query(Review).filter(Review.customer_id == customer_id).all()
    elif sneaker_id:
        return session.query(Review).filter(Review.sneaker_id == sneaker_id).all()
    else:
        return session.query(Review).all()

def get_unavailable_sneakers():
    return session.query(Sneaker).filter(Sneaker.is_available == False).all()

def delete_sneaker(sneaker_id):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        session.delete(sneaker)
        session.commit()
    return sneaker

def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
    return customer