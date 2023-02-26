from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from ..base import Base
from .category_image import CategoryImage


class ImagesInfo(Base):
    __tablename__ = "images_info"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    views_left = Column(Integer, nullable=True)
    last_view = Column(DateTime, nullable=True)
    category = relationship("Category", secondary=CategoryImage.__tablename__, back_populates="images_info")
