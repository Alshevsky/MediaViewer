from .category import Category
from .image_info import ImagesInfo

from ..base import Base, engine
from .services import new_session_started

Base.metadata.create_all(bind=engine)

new_session_started()
