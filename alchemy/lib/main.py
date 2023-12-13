from config import *

# CRUD OPERATIONS FOR THE USER

<<<<<<< HEAD
# Create of CRUD

def create_customer(first_name, last_name, email, contact):
    
    if not isinstance(contact, int) or not (1000000000 <= contact <= 9999999999):
        print("Kindly enter a valid 10-digit phone number")
        return None
    elif not isinstance(first_name, str) or not isinstance(last_name, str):
        print("Kindly enter a valid name")
        return None
    
    customer = Customer(first_name = first_name, last_name = last_name, email = email, contact = contact)
    
    session.add(customer)
    session.commit()
    
    return customer

def create_sneaker(brand, size, colour, price, is_available):
    
    if not isinstance(size, int) or not (1 <= size <= 15):
        print("Kindly enter a valid shoe size between 1 to 15")
        return None
    elif not isinstance(price, int) or not (50 <= price <= 5000):
        print("Kindly enter a valid sneaker price")
        return None
    
    sneaker = Sneaker(brand = brand, size = size, colour = colour, price = price, is_available = is_available)
    
    session.add(sneaker)
    session.commit()
    
    return sneaker

def create_review(customer_id, sneaker_id, rating):
    customer = session.query(Customer).get(customer_id)
    sneaker = session.query(Sneaker).get(sneaker_id)
    
    if customer is None:
        print("Customer not found")
        return None
    elif sneaker is None:
        print("Sneaker not found")
        return None
    elif not isinstance(rating, int) or not (1 <= rating <= 5):
        print("You can only enter a rating of between 1 to 5")
        return None
    
    review = Review(customer_id = customer_id, sneaker_id = sneaker_id, rating = rating)
    
    session.add(review)
    session.commit()
    
    return review
=======
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
>>>>>>> origin/brian
