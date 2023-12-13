from main import get_sneaker, get_customer, delete_customer, delete_sneaker
#from config import *
sneaker_id = 1
customer_id = 1

print()
print("***** Fetching sneaker by ID *****")
retrieved_sneaker = get_sneaker(sneaker_id)
print(f"Retrieved Sneaker => Brand: {retrieved_sneaker.brand}, ID: {retrieved_sneaker.id}, Price: {retrieved_sneaker.price}")

print("***** Fetching customer by ID *****")
retrieved_customer = get_customer(customer_id)
print(f"Retrieved Customer => Name: {retrieved_customer.first_name} {retrieved_customer.last_name}, ID: {retrieved_customer.id}, Email: {retrieved_customer.email}")

print("***** Delete customer by id *****")
deleted_customer = delete_customer(customer_id)
print(f"Deleted User => {deleted_customer.username}, ID => {deleted_customer.id}")

print("***** Delete sneaker by id *****")
deleted_user = delete_sneaker(sneaker_id)
print(f"Deleted User => {deleted_user.username}, ID => {deleted_user.id}")