import json
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.organizations import create_organization
from app.crud.organizations import get_organization_by_id

from app.core.vapaus_exception import VapausException


router = APIRouter()


class OrganizationPayload(BaseModel):
    email: str  # TODO: figure out how to get poetry to play nicely with pydantic EmailStr
    business_id: int


@router.post("/organizations", status_code=200)
def create(payload: OrganizationPayload, db: Session = Depends(get_db)) -> dict:
    """
    Create an organization object.
    """

    organization = create_organization(
        db,
        email=payload.email,
        business_id=payload.business_id
    )

    if organization is None:
        raise VapausException(
            status_code=422,
            error_code="ORGANIZATION_COULD_NOT_BE_CREATED",
            error_message="The organization couldn't be created.",
        )

    return JSONResponse(
        status_code=200,
        content={
            "organization": json.dumps(organization.as_dict(), indent=4, sort_keys=True, default=str)
        },
    )


@router.get("/organizations/{item_id}", status_code=200)
def get_bikes_for_organization(item_id: str, db: Session = Depends(get_db)) -> dict:
    """
    Get the bikes for an organization.
    """

    organization = get_organization_by_id(db, item_id)

    if organization is None:
        raise VapausException(
            status_code=422,
            error_code="ORGANIZATION_COULD_NOT_BE_FOUND",
            error_message="The organization couldn't be found.",
        )

    return JSONResponse(
        status_code=200,
        content={
            "bikes": json.dumps(organization.as_dict().bikes, sort_keys=True, default=str)
        },
    )


@router.get("/organizations/avgprice/{item_id}", status_code=200)
def get_average_price_for_organization(item_id: str, db: Session = Depends(get_db)) -> dict:
    """
    Get the average price for an organization.
    """

    organization = get_organization_by_id(db, item_id)

    if organization is None:
        raise VapausException(
            status_code=422,
            error_code="ORGANIZATION_COULD_NOT_BE_FOUND",
            error_message="The organization couldn't be found.",
        )

    avg = 0  # TODO: loop through organization.bikes.price

    return JSONResponse(
        status_code=200,
        content={
            "average_price": avg
        },
    )
