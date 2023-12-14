from config import *

# CRUD OPERATIONS FOR THE USER

 # CREATE!!!
# create new customer
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
# create new sneaker
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
# create new review
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


 # UPDATE!!!
# ----update sneaker price
def update_sneaker_price(sneaker_id, new_price):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        sneaker.price = new_price
        session.commit()
    return sneaker

def get_sneaker(sneaker_id):
    return session.query(Sneaker).get(sneaker_id)
# update sneaker availabilty
def update_sneaker_availability(sneaker_id, new_availability):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        sneaker.is_available = new_availability
        session.commit()
    return sneaker

# ----update customer info
def update_customer_info(customer_id, updated_info):
    customer = session.query(Customer).get(customer_id)
    if customer:
        for key, value in updated_info.items():
            setattr(customer, key, value)
        session.commit()
    return customer

def get_customer(customer_id):
    return session.query(Customer).get(customer_id)

 # READ!!!
# read sneaker details
def get_sneaker(sneaker_id):
    return session.query(Sneaker).get(sneaker_id)
# read customer details
def get_customer(customer_id):
    return session.query(Customer).get(customer_id)
# read review associated with a particular customer/sneaker
def get_reviews(customer_id=None, sneaker_id=None):
    if customer_id:
        return session.query(Review).filter(Review.customer_id == customer_id).all()
    elif sneaker_id:
        return session.query(Review).filter(Review.sneaker_id == sneaker_id).all()
    else:
        return session.query(Review).all()
# read unavailable sneakers
def get_unavailable_sneakers():
    return session.query(Sneaker).filter(Sneaker.is_available == False).all()


 # DELETE!!!
# delete sneaker by id
def delete_sneaker(sneaker_id):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
        session.query(Review).filter(Review.sneaker_id == sneaker_id).delete()
        session.delete(sneaker)
        session.commit()
    return sneaker
# delete customer by id
def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.query(Review).filter(Review.customer_id == customer_id).delete()
        session.delete(customer)
        session.commit()
    return customer

