from fastapi import FastAPI

from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from .settings import DIR_TEMPLATES_PATH

app = FastAPI()
app.mount("/data", StaticFiles(directory="data"), name="data")
templates = Jinja2Templates(DIR_TEMPLATES_PATH)
