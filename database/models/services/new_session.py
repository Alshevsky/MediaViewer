import csv

from sqlalchemy.orm import Session

from app.settings import FILE_CSV_PATH
from database.base import engine

from ..image_info import ImagesInfo
from ..category_image import CategoryImage
from ..category import Category


def new_session_started():
    image_name_row_id = 0
    image_views_left_row_id = 1
    categories_row_id = 2
    data: dict[str: list[str]] = {}

    with Session(engine) as session:
        session.query(ImagesInfo).delete()
        session.query(CategoryImage).delete()
        session.query(Category).delete()
        session.commit()

        with open(FILE_CSV_PATH, encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=";")
            if file_reader:
                for row in file_reader:
                    image_data = ImagesInfo(
                        title=row[image_name_row_id],
                        views_left=int(row[image_views_left_row_id]),
                    )
                    session.add(image_data)
                    session.commit()

                    for category_name in row[categories_row_id:]:
                        category_instance = Category(name=category_name)

                        if session.query(Category).where(Category.name == category_name).first() is None:
                            session.add(category_instance)
                            session.commit()

                    data[image_data.title] = row[categories_row_id:]
    # Поскольку при добавлении М2М падала ошибка IntegrityError, БД не могла закоммититься.
    # Пришлось категории добавлять к изображениям в отдельной сессии.
    with Session(engine) as session:
        for key, value in data.items():
            image: ImagesInfo = session.query(ImagesInfo).filter(ImagesInfo.title == key).first()
            categories = session.query(Category).filter(Category.name.in_(value)).all()
            image.category = categories
            session.commit()
