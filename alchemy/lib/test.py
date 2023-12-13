from main import (
    update_sneaker_price,
    update_sneaker_availability,
    get_sneaker,
    update_customer_info,
    get_customer
)

# ===== SNEAKER UPDATE
print(">>>>>>>>>>>> SNEAKER UPDATE OPERATIONS <<<<<<<<<<<")
sneaker_id = 1

print("***** Fetching sneaker by ID *****")
retrieved_sneaker = get_sneaker(sneaker_id)
if retrieved_sneaker:
    print(f"Retrieved Sneaker => Brand: {retrieved_sneaker.brand}, ID: {retrieved_sneaker.id}, Price: {retrieved_sneaker.price}")
    
    # update sneaker price
    print("***** Update Sneaker Price *****")
    updated_sneaker_price = 2000
    update_sneaker_price(sneaker_id, updated_sneaker_price)
    print(f"Updated Sneaker Price => Brand: {retrieved_sneaker.brand}, ID: {retrieved_sneaker.id}, Updated Price: {updated_sneaker_price}")

    # update sneaker availability
    print("***** Update Sneaker Availability *****")
    updated_sneaker_availability = False
    update_sneaker_availability(sneaker_id, updated_sneaker_availability)
    print(f"Updated Sneaker Availability => Brand: {retrieved_sneaker.brand}, ID: {retrieved_sneaker.id}, Updated Availability: {updated_sneaker_availability}")

# ===== CUSTOMER UPDATE
print()
print(">>>>>>>>>>>> CUSTOMER UPDATE OPERATIONS <<<<<<<<<<<")
customer_id = 1

     # fetch customer using there id
print("***** Fetching customer by ID *****")
retrieved_customer = get_customer(customer_id)
if retrieved_customer:
    print(f"Retrieved Customer => Name: {retrieved_customer.first_name} {retrieved_customer.last_name}, ID: {retrieved_customer.id}, Email: {retrieved_customer.email}")

        # update the customer info
    print("***** Update Customer Info *****")
    updated_customer_info = {'first_name': 'Brian', 'last_name': 'Cherus', 'email': 'Brian@gmail.com', 'contact': 987654321}
    update_customer_info(customer_id, updated_info=updated_customer_info)

