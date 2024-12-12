from faker import Faker
from schemas.book_schemas import books as bks, ReadBook
from schemas.record_schemas import ReadBorrowRecord, records as rcs
from schemas.user_schemas import users as usrs, ReadUser
import random

user_ids = []
book_ids = []

fake = Faker()

# Utility for generating unique 4-digit IDs
def generate_id(prefix):
    if prefix == 'user':
        id= f"us_{len(usrs) + 1:04}"
        user_ids.append(id)
        return id
    elif prefix == 'book':
        id= f"bk_{len(bks) + 1:04}"
        book_ids.append(id)
        return id
    elif prefix == 'record':
        id= f"rc_{len(rcs) + 1:04}"
        return id

# Populating test data
def generate_users(num):
    for _ in range(num):
        user = ReadUser(
            id=generate_id("user"),
            name=fake.name(),
            email=fake.email(),
            is_active=True
        )
        usrs.update({user.id: user})

def generate_books(num):
    for _ in range(num):
        book = ReadBook(
            id=generate_id("book"),
            title=f"{fake.word().capitalize()} {fake.word().capitalize()}",
            author=fake.name(),
            is_available=True
        )
        bks.update({book.id: book})

def generate_records(num):
    for _ in range(num):
        record = ReadBorrowRecord(
            id=generate_id("record"),
            user_id= random.choice(user_ids),
            book_id= random.choice(book_ids),
            borrowed_at= fake.date_this_decade(),
            returned_at= None,
            is_available= False
        )
        rcs.update({record.id: record})

# Function to generate initial data
def generate_initial_data():
    generate_users(10)
    generate_books(20)
    generate_records(50)


if __name__ == "__main__":
    generate_initial_data()