from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.bike import Bike


def create_bike(db: Session, email: str):
    bike = Bike(email=email)

    db.add(bike)
    db.commit()
    db.refresh(bike)

    return bike


def get_bike_by_email(db: Session, email: str):
    result = db.scalars(
        select(Bike).where(Bike.email == email)
    ).one_or_none()
    return result


def update_bike(
    db: Session,
    bike: Bike,
    **kwargs
):
    for key, value in kwargs.items():
        setattr(bike, key, value)

    db.add(bike)
    db.commit()
    db.refresh(bike)

    return bike
