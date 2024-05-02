from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CapturedImageModel(Base):
    __tablename__ = 'captured_images'

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    mouse_x = Column(Integer, nullable=False)
    mouse_y = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    image_source = Column(LargeBinary, nullable=True)
