import json
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.bikes import create_bike
from app.crud.bikes import get_bike_by_id
from app.crud.bikes import update_bike

from app.core.vapaus_exception import VapausException


router = APIRouter()


class BikePayload(BaseModel):
    organization: int
    brand: str
    model: str
    price: float
    serial_number: int


@router.post("/bikes", status_code=200)
def create(payload: BikePayload, db: Session = Depends(get_db)) -> dict:
    """
    Create a bike object.
    """
    # email = payload.email

    bike = create_bike(
        db,
        organization=payload.organization,
        brand=payload.brand,
        model=payload.model,
        price=payload.price,
        serial_number=payload.serial_number
    )

    if bike is None:
        raise VapausException(
            status_code=422,
            error_code="BIKE_COULD_NOT_BE_CREATED",
            error_message="The bike couldn't be created.",
        )

    return JSONResponse(
        status_code=200,
        content={
            "bike": json.dumps(bike.as_dict(), indent=4, sort_keys=True, default=str)
        },
    )


@router.get("/bikes/{item_id}", status_code=200)
def get(item_id: str, db: Session = Depends(get_db)) -> dict:
    """
    Get a bike object by id.
    """

    bike = get_bike_by_id(db, item_id)

    if bike is None:
        raise VapausException(
            status_code=422,
            error_code="BIKE_COULD_NOT_BE_FOUND",
            error_message="The bike couldn't be found.",
        )

    return JSONResponse(
        status_code=200,
        content={
            "bike": json.dumps(bike.as_dict(), sort_keys=True, default=str)
        },
    )


@router.patch("/bikes/{item_id}", status_code=200)
def update(item_id: str, payload: BikePayload, db: Session = Depends(get_db)) -> dict:
    """
    Update a bike object by id.
    """
    email = payload.email
    old_bike = get_bike_by_id(db, item_id)

    if old_bike is None:
        raise VapausException(
            status_code=422,
            error_code="BIKE_COULD_NOT_BE_FOUND",
            error_message="The bike couldn't be found.",
        )

    bike = update_bike(db, old_bike, email=email)

    return JSONResponse(
        status_code=200,
        content={
            "bike": json.dumps(bike.as_dict(), indent=4, sort_keys=True, default=str)
        },
    )
