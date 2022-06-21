import datetime
from sqlalchemy import Column, ForeignKey, Float, DateTime, Integer, String, null

from app.db.base_model import BaseModel


class Bike(BaseModel):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=True, default=null())
    price = Column(Float, nullable=False)
    serial_number = Column(Integer, index=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now,
        nullable=False
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
