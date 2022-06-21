import datetime
import secrets
import string
from sqlalchemy import Column, DateTime, Integer, String, null
from sqlalchemy.orm import relationship

from app.db.base_model import BaseModel


def create_code():
    return "".join(secrets.choice(string.digits) for i in range(6))


class Organization(BaseModel):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True, nullable=False)
    business_id = Column(Integer, index=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        nullable=False
    )
    bikes = relationship("Bike")
