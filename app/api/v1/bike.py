import json
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.bikes import create_bike
from app.crud.bikes import get_bike_by_email

from app.core.vapaus_exception import VapausException


router = APIRouter()


class VerifyPayload(BaseModel):
    email: str


@router.post("/bikes", status_code=200)
def create(payload: VerifyPayload, db: Session = Depends(get_db)) -> dict:
    """
    Create a bike object.
    """
    email = payload.email

    bike = create_bike(db, email)

    if bike is None:
        raise VapausException(
            status_code=422,
            error_code="BIKE_COULD_NOT_BE_CREATED",
            error_message="The bike couldn't be created.",
        )

    print(f"✅🚲 Created bike {bike.email} at {bike.created_at}")

    return JSONResponse(
        status_code=200,
        content={
            "bike": json.dumps(bike.as_dict(), indent=4, sort_keys=True, default=str)
        },
    )


@router.get("/bikes/{item_id}", status_code=200)
def get_bike(item_id: str, db: Session = Depends(get_db)) -> dict:
    """
    Get a bike object by id.
    """

    bike = get_bike_by_email(db, item_id)

    if bike is None:
        raise VapausException(
            status_code=422,
            error_code="BIKE_COULD_NOT_BE_FOUND",
            error_message="The bike couldn't be found.",
        )

    return JSONResponse(
        status_code=200,
        content={
            "bike": json.dumps(bike.as_dict(), indent=4, sort_keys=True, default=str)
        },
    )
