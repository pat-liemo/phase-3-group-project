from config import *

# CRUD OPERATIONS FOR THE USER

# ----CRUD Operations for Sneaker
def update_sneaker_price(sneaker_id, new_price):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        sneaker.price = new_price
        session.commit()
    return sneaker

def get_sneaker(sneaker_id):
    return session.query(Sneaker).get(sneaker_id)

def update_sneaker_availability(sneaker_id, new_availability):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        sneaker.is_available = new_availability
        session.commit()
    return sneaker

# ----CRUD Operations for Customer
def update_customer_info(customer_id, updated_info):
    customer = session.query(Customer).get(customer_id)
    if customer:
        for key, value in updated_info.items():
            setattr(customer, key, value)
        session.commit()
    return customer

def get_customer(customer_id):
    return session.query(Customer).get(customer_id)
