from database import Base
from sqlalchemy import (Column, String, Integer, UUID)
import uuid


class ShortUrl(Base):
    __tablename__ = 'short_urls'
    id = Column(UUID, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    url = Column(String(1000), nullable=False, default='')
