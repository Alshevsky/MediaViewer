from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from ..base import Base
from .category_image import CategoryImage


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    images_info = relationship("ImagesInfo", secondary=CategoryImage.__tablename__, back_populates="category")
