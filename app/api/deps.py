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


def populate_organizations():
    # TODO: use the data files to populate the orgs
    print("STUB: populate_organizations")


def populate_bikes():
    # TODO: use the data files to populate the bikes
    print("STUB: populated bikes")
