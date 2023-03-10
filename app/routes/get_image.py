from fastapi import Query
from starlette.requests import Request

from ..main import app, templates
from ..actions import get_image_name, get_image_path, parse_query_request


@app.get("/")
async def get_image(
    request: Request, query: list[str] | None = Query(description="Category search", deprecated=False, default=None)
):
    category_list = await parse_query_request(query)
    image_name = await get_image_name(category_list)
    image_path = await get_image_path(image_name)
    return templates.TemplateResponse("index.html", {"request": request, "image": image_path})
