import os

from datetime import datetime

from sqlalchemy.orm import Session
from database import ImagesInfo, Category, engine

from ..settings import PLACEHOLDER_IMAGE_NAME, MEDIA_PATH, STATIC_PATH


async def get_image_name(categories: list[str] | None) -> str:
    with Session(engine) as session:
        query = session.query(ImagesInfo)
        if categories:
            image = (
                query.filter(ImagesInfo.category.any(Category.name.in_(categories)), ImagesInfo.views_left > 0)
                .order_by(ImagesInfo.last_view)
                .first()
            )
        else:
            image = query.filter(ImagesInfo.views_left > 0).order_by(ImagesInfo.last_view).first()

    if image:
        with Session(engine) as session:
            session.query(ImagesInfo).filter(ImagesInfo.title == image.title).update(
                {
                    "last_view": datetime.now(),
                    "views_left": (image.views_left - 1),
                }
            )
            session.commit()
        return image.title

    return PLACEHOLDER_IMAGE_NAME


async def get_image_path(image_name: str) -> str:
    if image_name == PLACEHOLDER_IMAGE_NAME:
        return os.path.join(STATIC_PATH, image_name)
    return os.path.join(MEDIA_PATH, image_name)


async def parse_query_request(value: list[str] | None) -> list | None:
    category_names = []
    for element in value:
        category_names.extend(element.split(","))
    return [name.strip() for name in category_names if name]
