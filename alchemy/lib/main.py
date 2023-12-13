from config import *

# CRUD OPERATIONS FOR THE USER

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

