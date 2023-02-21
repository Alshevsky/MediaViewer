from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    name: str


class Images(BaseModel):
    title: str
    amount_of_shows: int
    categories: List[Category] | None


class CategoryList(BaseModel):
    name: List[str] | None
