from faker import Faker
from schemas.book_schemas import books as bks
from schemas.record_schemas import records as rcs
from schemas.user_schemas import users as usrs

# bks={}
# rcs={}
# usrs={}

fake = Faker()

# Utility for generating unique 4-digit IDs
def generate_id(prefix):
    if prefix == 'user':
        return f"us_{len(usrs) + 1:04}"
    elif prefix == 'book':
        return f"bk_{len(bks) + 1:04}"
    elif prefix == 'record':
        return f"rc_{len(rcs) + 1:04}"

# Populating test data
def generate_users(num):
    for _ in range(num):
        user = {"id": generate_id("user"), "name": fake.name(), "email": fake.email(), "is_active": True}
        usrs.update({user["id"]: user})

def generate_books(num):
    for _ in range(num):
        book = {"id": generate_id("book"), "title": fake.word().capitalize(), "author": fake.name(), "is_available": True}
        bks.update({book["id"]: book})

# Function to generate initial data
def generate_initial_data():
    generate_users(10)
    generate_books(20)


if __name__ == "__main__":
    generate_initial_data()