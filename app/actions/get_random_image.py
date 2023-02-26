import csv
import os

from datetime import datetime

from sqlalchemy.orm import Session
from database import ImagesInfo, engine

from ..settings import FILE_CSV_PATH, PLACEHOLDER_IMAGE_NAME, MEDIA_PATH, STATIC_PATH


async def get_image_name(category: list[str] | None) -> str:
    images_list = None

    if os.path.isfile(FILE_CSV_PATH):
        with open(FILE_CSV_PATH, encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=";")

            images_list = [element for element in file_reader]
            if category:
                images_list = list(filter(lambda image: bool(set(category) & set(image[2:])), images_list))

    if images_list:
        title_images = [image[0] for image in images_list]
        with Session(engine) as session:
            images = session.query(ImagesInfo).where(ImagesInfo.title.in_(title_images)).all()

        if images:
            available_images = list(filter(lambda instance: instance.views_left > 0, images))

            if available_images:
                no_views_images = list(filter(lambda instance: instance.last_view is None, available_images))

                if no_views_images:
                    filtered_images = no_views_images
                else:
                    available_images.sort(key=lambda instance: instance.last_view)
                    filtered_images = available_images

                result = filtered_images[0]
                with Session(engine) as session:
                    session.query(ImagesInfo).filter(ImagesInfo.title == result.title).update(
                        {
                            "last_view": datetime.now(),
                            "views_left": (result.views_left - 1),
                        }
                    )
                    session.commit()

                return result.title
    return PLACEHOLDER_IMAGE_NAME


async def get_image_path(image_name: str) -> str:
    if image_name == PLACEHOLDER_IMAGE_NAME:
        return os.path.join(STATIC_PATH, image_name)
    return os.path.join(MEDIA_PATH, image_name)
