import datetime
import secrets
import string
from sqlalchemy import Column, DateTime, Integer, String, null

from app.db.base_model import BaseModel


def create_code():
    return "".join(secrets.choice(string.digits) for i in range(6))


class Bike(BaseModel):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        nullable=False
    )
    verified_at = Column(DateTime(timezone=True), default=null())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
