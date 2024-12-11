from schemas.user_schemas import WriteUser, ReadUser, UpdateUser, users
from fastapi import HTTPException

class UserCrud:
    @staticmethod
    def create_user(user_data: WriteUser):
        user_id = f"us_{len(users) + 1:04}"
        user = ReadUser(id=user_id, **user_data.dict())
        users[user_id] = user
        return user

    @staticmethod
    def get_user(user_id: str):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_all_users():
        return list(users.values())

    @staticmethod
    def update_user(user_id: str, user_data: UpdateUser):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        users[user_id] = user
        return user

    @staticmethod
    def delete_user(user_id: str):
        user = users.pop(user_id, None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

user_crud = UserCrud()