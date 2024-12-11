from fastapi import APIRouter
from crud.user_crud import user_crud
from schemas.user_schemas import UpdateUser, WriteUser

users_router = APIRouter()

@users_router.post("/create", status_code=201)
async def create_user_endpoint(user_data: WriteUser):
    return user_crud.create_user(user_data)

@users_router.get("/{user_id}", status_code=200)
async def get_user_endpoint(user_id: str):
    return user_crud.get_user(user_id)

@users_router.get("/get/all", status_code=200)
async def get_all_users_endpoint():
    return user_crud.get_all_users()

@users_router.patch("/update/partial/{user_id}", status_code=200)
async def partial_update_user_endpoint(user_id: str, user_data: UpdateUser):
    return user_crud.update_user(user_id, user_data)

@users_router.put("/update/full/{user_id}", status_code=200)
async def full_update_user_endpoint(user_id: str, user_data: WriteUser):
    return user_crud.update_user(user_id, user_data)

@users_router.patch("/deactivate/{user_id}", status_code=200)
async def deactivate_user_endpoint(user_id: str):
    return user_crud.deactivate_user(user_id)

@users_router.delete("/delete/{user_id}", status_code=200)
async def delete_user_endpoint(user_id: str):
    return user_crud.delete_user(user_id)