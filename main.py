from fastapi import FastAPI
from routers import user_routes, book_routes, record_routes
from services import fake_data

app = FastAPI()

fake_data.generate_initial_data()

app.include_router(user_routes.users_router, prefix="/user", tags=["Users"])
app.include_router(book_routes.books_router, prefix="/book", tags=["Books"])
app.include_router(record_routes.records_router, prefix="/record", tags=["Records"])