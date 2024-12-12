import logging
from schemas.record_schemas import records
from fastapi import HTTPException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CRUDOperations")

class RecordCrud:
    @staticmethod
    def get_all_records():
        logger.info("Fetching all records.")
        return list(records.values()) or []
    
    @staticmethod
    def get_user_record(user_id: str):
        logger.info(f"Fetching record for user: {user_id}")
        record = [record for record in records.values() if record.user_id == user_id]
        if not record:
            logger.warning(f"No record found for user: {user_id}")
            raise HTTPException(status_code=404, detail="Record not found")
        logger.info(f"Record found for user: {user_id}")
        return record
    
    @staticmethod
    def get_book_record(book_id: str):
        logger.info(f"Fetching record for book: {book_id}")
        record = [record for record in records.values() if record.book_id == book_id]
        if not record:
            logger.warning(f"No record found for book: {book_id}")
            raise HTTPException(status_code=404, detail="Record not found")
        logger.info(f"Record found for book: {book_id}")
        return record

    @staticmethod
    def get_record(record_id: str):
        logger.info(f"Fetching record with ID: {record_id}")
        record = records.get(record_id)
        if not record:
            logger.warning(f"Record with ID {record_id} not found.")
            raise HTTPException(status_code=404, detail="Record not found")
        logger.info(f"Record with ID {record_id} found.")
        return record

record_crud = RecordCrud()
