from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from app.db.base import BaseModel


engine = create_engine(
    'postgresql+psycopg2://postgres:db580f2e939baa98cb393fa1b680c6b17072ff1b42b0669f575c0f93e525a8d3@db/vapaus'
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create all tables, if they don't exist, every time the app starts
metadata = BaseModel.metadata  # type: ignore
metadata.create_all(engine)
