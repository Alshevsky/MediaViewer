from pydantic import BaseModel


class Category(BaseModel):
    name: str


class Images(BaseModel):
    title: str
    amount_of_shows: int
    categories: list[Category] | None


class CategoryList(BaseModel):
    name: list[str] | None
