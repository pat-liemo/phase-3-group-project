from config import *

# Retrieve details about a specific sneaker using its ID
def get_sneaker(sneaker_id):
    return session.query(Sneaker).get(sneaker_id)

# Retrieve details about a specific customer using their ID
def get_customer(customer_id):
    return session.query(Customer).get(customer_id)

# Fetch all reviews associated with a particular customer/sneaker or all reviews
def get_reviews(customer_id=None, sneaker_id=None):
    if customer_id:
        # Fetch reviews based on customer ID
        return session.query(Review).filter(Review.customer_id == customer_id).all()
    elif sneaker_id:
        # Fetch reviews based on sneaker ID
        return session.query(Review).filter(Review.sneaker_id == sneaker_id).all()
    else:
        # Fetch all reviews if no specific IDs provided
        return session.query(Review).all()

# Fetch all unavailable sneakers for restocking
def get_unavailable_sneakers():
    return session.query(Sneaker).filter(Sneaker.is_available == False).all()

# Delete a specific sneaker by providing its ID
def delete_sneaker(sneaker_id):
    sneaker = session.query(Sneaker).get(sneaker_id)
    if sneaker:
     # Delete the sneaker from the database
        session.delete(sneaker)
        session.commit()
    return sneaker

# Delete a specific customer by providing their ID
def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        # Delete the customer from the database
        session.delete(customer)
        session.commit()
    return customer