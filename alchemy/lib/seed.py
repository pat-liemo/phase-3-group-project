from config import *
from datetime import datetime, timedelta
import random

fake = Faker()

session.query(Sneaker).delete()
session.query(Customer).delete()
session.query(Review).delete()
session.commit()

print("SEEDING SNEAKERS...")
def seed_sneaker():
    sneakers = [
        Sneaker(
            brand = fake.company(),
            size=fake.random_int(min=1, max=15), 
            colour=fake.color_name(),
            price=fake.random_int(min=50, max=1000),
            is_available=fake.boolean()
        )
        
        for _ in range(30)
    ]
    
    session.add_all(sneakers)
    session.commit()
    
seed_sneaker()



print("SEEDING CUSTOMERS...")
def seed_customer():
    customers = [
        Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email = fake.email(),
            contact = fake.random_number(digits = 10)
        )
        
        for _ in range(30)
    ]
    
    session.add_all(customers)
    session.commit()
    
seed_customer()

start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


print("SEEDING REVIEWS...")
def seed_review():
    all_customers = session.query(Customer).all()
    all_sneakers = session.query(Sneaker).all()
    
    reviews = [
        Review(
            customer_id = fake.random_element(elements = all_customers).id,
            sneaker_id = fake.random_element(elements = all_sneakers).id,
            rating = fake.random_int(min=1, max=5),
            created_at = random_date(start_date, end_date)
        )
        
        for _ in range(30)
    ]
    
    session.add_all(reviews)
    session.commit()
    
seed_review()

session.close()
print("=== SEEDING COMPLETE ===")