from schemas.user_schemas import WriteUser, ReadUser, UpdateUser, users
from fastapi import HTTPException
from services.fake_data import generate_id

class UserCrud:
    @staticmethod
    def create_user(user_data: WriteUser):
        try:
            user_id = generate_id("user")
            user = ReadUser(id=user_id, **user_data.model_dump())
            users[user_id] = user
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user(user_id: str):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_all_users():
        return list(users.values()) or []

    @staticmethod
    def update_user(user_id: str, user_data: UpdateUser):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        try:
            for key, value in user_data.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            users[user_id] = user
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def deactivate_user(user_id: str):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        return user

    @staticmethod
    def delete_user(user_id: str):
        user = users.pop(user_id, None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

user_crud = UserCrud()