from faker import Faker
import random
from schemas.book_schemas import books as bks
from schemas.record_schemas import records as rcs
from schemas.user_schemas import users as usrs

fake = Faker()

# Utility for generating unique 4-digit IDs
def generate_id(prefix):
    if prefix == 'us':
        return f"us_{len(usrs) + 1:04}"
    elif prefix == 'bk':
        return f"bk_{len(bks) + 1:04}"
    elif prefix == 'rc':
        return f"rc_{len(rcs) + 1:04}"

# Populating test data
def generate_users(num=10):
    users = [{"id": generate_id("us"), "name": fake.name(), "email": fake.email(), "is_active": True} for _ in range(num)]
    usrs.update({user["id"]: user for user in users})

def generate_books(num=20):
    books = [{"id": generate_id("bk"), "title": fake.word().capitalize(), "author": fake.name(), "is_available": True} for _ in range(num)]
    bks.update({book["id"]: book for book in books})

# Function to generate initial data
def generate_initial_data():
    generate_users()
    generate_books()

if __name__ == "__main__":
    generate_initial_data()