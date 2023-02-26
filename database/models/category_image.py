from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class CategoryImage(Base):
    __tablename__ = "category_image"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    images_info_id = Column(Integer, ForeignKey("images_info.id"))
