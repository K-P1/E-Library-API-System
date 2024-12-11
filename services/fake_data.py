from faker import Faker
import random

fake = Faker()

users = []
books = []
records = []

# Utility for generating unique 4-digit IDs
def generate_id(prefix):
    return f"{prefix}_{str(random.randint(1000, 9999))}"

# Populating test data
def generate_users(num=10):
    global users
    users = [{"id": generate_id("us"), "name": fake.name(), "email": fake.email(), "is_active": True} for _ in range(num)]

def generate_books(num=20):
    global books
    books = [{"id": generate_id("bk"), "title": fake.word().capitalize(), "author": fake.name(), "is_available": True} for _ in range(num)]

# Generate initial data
generate_users()
generate_books()