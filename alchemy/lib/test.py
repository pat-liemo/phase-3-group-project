from main import update_sneaker_price, update_sneaker_availability, get_sneaker, update_customer_info, get_customer, get_sneaker, get_customer, delete_customer, delete_sneaker, get_reviews, get_unavailable_sneakers

# READ!!!
# Individual IDs for sneaker and customer details
sneaker_id = 15
customer_id = 14
print()
print("***** Fetching sneaker details by ID *****")
retrieved_sneaker = get_sneaker(sneaker_id)
print(f"Retrieved Sneaker => Brand: {retrieved_sneaker.brand}, ID: {retrieved_sneaker.id}, Price: {retrieved_sneaker.price}")

print("***** Fetching customer details by ID *****")
retrieved_customer = get_customer(customer_id)
print(f"Retrieved Customer => Name: {retrieved_customer.first_name} {retrieved_customer.last_name}, ID: {retrieved_customer.id}, Email: {retrieved_customer.email}")

# Fetch reviews
customer_id_for_reviews = 17
sneaker_id_for_reviews = 18

print("***** Fetching reviews by Customer ID *****")
reviews_by_customer = get_reviews(customer_id=customer_id_for_reviews)
print(f"Reviews by Customer ID {customer_id_for_reviews}: {[review.rating for review in reviews_by_customer]}")

print("***** Fetching reviews by Sneaker ID *****")
reviews_by_sneaker = get_reviews(sneaker_id=sneaker_id_for_reviews)
print(f"Reviews by Sneaker ID {sneaker_id_for_reviews}: {[review.rating for review in reviews_by_sneaker]}")

# Fetch unavailable sneakers
print("***** Fetching unavailable sneakers *****")
unavailable_sneakers = get_unavailable_sneakers()
print(f"Unavailable Sneakers: {[sneaker.brand for sneaker in unavailable_sneakers]}")



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

        # update customer info
    print("***** Update Customer Info *****")
    updated_customer_info = {'first_name': 'Brian', 'last_name': 'Cherus', 'email': 'Brian@gmail.com', 'contact': 987654321}
    update_customer_info(customer_id, updated_info=updated_customer_info)


    
  # DELETE TEST
# Individual IDs for deleting customer/sneaker by id
customer_id_for_delete = 3
sneaker_id_for_delete = 8
print("***** Delete customer by id *****")
deleted_customer = delete_customer(customer_id_for_delete)
print(f"Deleted Customer => Name: {deleted_customer.first_name} {deleted_customer.last_name}, ID: {deleted_customer.id}")

print("***** Delete sneaker by id *****")
deleted_sneaker = delete_sneaker(sneaker_id_for_delete)
print(f"Deleted Sneaker => Brand: {deleted_sneaker.brand}, ID: {deleted_sneaker.id}")


