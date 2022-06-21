from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.organization import Organization


def create_organization(db: Session, **kwargs):
    organization = Organization()
    for key, value in kwargs.items():
        setattr(organization, key, value)

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization


def get_organization_by_id(db: Session, id: int):
    result = db.scalars(
        select(Organization).where(Organization.id == id)
    ).one_or_none()
    return result


def update_organization(
    db: Session,
    organization: Organization,
    **kwargs
):
    for key, value in kwargs.items():
        setattr(organization, key, value)

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization
