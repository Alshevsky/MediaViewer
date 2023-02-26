import csv

from ..schemas import Images
from ..settings import FILE_CSV_PATH

from sqlalchemy.orm import Session
from database import ImagesInfo, engine


async def add_image_to_csv(item: Images, category_list: list[str] | None) -> None:
    values_list = [item.title, item.amount_of_shows]
    if category_list:
        values_list.extend(category_list)

    with open(FILE_CSV_PATH, mode="a+", encoding="utf-8") as file:
        file_write = csv.writer(file, delimiter=";")
        file_write.writerow(values_list)

    with Session(engine) as session:
        instance = ImagesInfo(
            title=item.title,
            views_left=item.amount_of_shows,
        )
        session.add(instance)
        session.commit()
