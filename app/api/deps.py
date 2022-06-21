from typing import Generator

from app.db.database import Session


def get_db() -> Generator:
    """
    Return an sqlalchemy session. To be used with FastAPI's "Depends()"
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
