from fastapi import UploadFile, Response
from sqlalchemy.orm import Session

from database import ImagesInfo, engine

from ..main import app
from ..schemas import Images
from ..actions import add_image_to_csv, write_media_file


@app.post("/")
async def create_image(file: UploadFile, amount_of_shows: int, category_list: list[str] | None) -> Response:
    with Session(engine) as session:
        value_exists = session.query(
            session.query(ImagesInfo).filter(ImagesInfo.title == file.filename).exists()
        ).scalar()
    if value_exists:
        return Response(status_code=400)

    image = Images(
        title=file.filename,
        amount_of_shows=amount_of_shows,
    )
    category_list = category_list[0].split(",") if category_list else None
    await add_image_to_csv(image, category_list)
    await write_media_file(file)
    return Response(status_code=204)
