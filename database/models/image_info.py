import csv

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import Session

from app.settings import FILE_CSV_PATH
from ..base import Base, engine


class ImagesInfo(Base):
    __tablename__ = "images_info"

    title = Column(String, primary_key=True, unique=True, index=True)
    views_left = Column(Integer, nullable=True)
    last_view = Column(DateTime, nullable=True)


Base.metadata.create_all(bind=engine)


def new_session_started():
    with Session(engine) as session:
        session.query(ImagesInfo).delete()
        session.commit()

        with open(FILE_CSV_PATH, encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=";")
            if file_reader:
                for row in file_reader:
                    new_data = ImagesInfo(
                        title=row[0],
                        views_left=int(row[1]),
                    )
                    session.add(new_data)
                    session.commit()


new_session_started()
