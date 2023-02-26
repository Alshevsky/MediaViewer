import os
import aiofiles

from fastapi import File

from ..settings import MEDIA_PATH


async def write_media_file(file: File) -> None:
    file_path = os.path.join(MEDIA_PATH, file.filename)
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
