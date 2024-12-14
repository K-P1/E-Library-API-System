import logging
from schemas.user_schemas import WriteUser, ReadUser, UpdateUser, users
from fastapi import HTTPException
from services.fake_data import generate_id

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CRUDOperations")

class UserCrud:
    @staticmethod
    def create_user(user_data: WriteUser):
        try:
            logger.info("Attempting to create a new user.")
            user_id = generate_id("user")
            user = ReadUser(id=user_id, **user_data.model_dump())
            users[user_id] = user
            logger.info(f"User created successfully with ID: {user_id}")
            return user
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user(user_id: str):
        logger.info(f"Fetching user with ID: {user_id}")
        user = users.get(user_id)
        if not user:
            logger.warning(f"User with ID {user_id} not found.")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"User with ID {user_id} found.")
        return user

    @staticmethod
    def get_all_users():
        logger.info("Fetching all users.")
        logger.info(f"Number of users found: {len(users)}")
        return list(users.values()) or []

    @staticmethod
    def update_user(user_id: str, user_data: UpdateUser):
        logger.info(f"Attempting to update user with ID: {user_id}")
        user = users.get(user_id)
        if not user:
            logger.warning(f"User with ID {user_id} not found.")
            raise HTTPException(status_code=404, detail="User not found")
        try:
            for key, value in user_data.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            users[user_id] = user
            logger.info(f"User with ID {user_id} updated successfully.")
            return user
        except Exception as e:
            logger.error(f"Error updating user with ID {user_id}: {e}")
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def deactivate_user(user_id: str):
        logger.info(f"Deactivating user with ID: {user_id}")
        user = users.get(user_id)
        if not user:
            logger.warning(f"User with ID {user_id} not found.")
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        logger.info(f"User with ID {user_id} deactivated successfully.")
        return user

    @staticmethod
    def delete_user(user_id: str):
        logger.info(f"Attempting to delete user with ID: {user_id}")
        user = users.pop(user_id, None)
        if not user:
            logger.warning(f"User with ID {user_id} not found.")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"User with ID {user_id} deleted successfully.")
        return user

user_crud = UserCrud()