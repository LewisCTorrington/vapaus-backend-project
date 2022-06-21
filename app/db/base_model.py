from sqlalchemy import Column, Integer

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel:
    # all models should have an "id"
    id = Column(Integer, primary_key=True, index=True)
