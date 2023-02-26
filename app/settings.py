import os

from environs import Env

env = Env()

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
env.read_env(os.path.join(BASE_DIR, ".env"), recurse=True)

DB_PATH = os.path.join(BASE_DIR, "database", "DB")

# Env Datas
FILE_CSV_NAME = env.str("FILE_NAME", "images_data.csv")
DB_URL = env.str("DATABASE_URL")

# Main paths
DIR_DATA_PATH = os.path.join(BASE_DIR, "data")
DIR_TEMPLATES_PATH = os.path.join(BASE_DIR, "templates")
FILE_CSV_PATH = os.path.join(DIR_DATA_PATH, FILE_CSV_NAME)
MEDIA_PATH = os.path.join("data", "images")
STATIC_PATH = os.path.join("data", "static")

# Other
PLACEHOLDER_IMAGE_NAME = "404.jpeg"

if not os.path.exists(DIR_DATA_PATH):
    os.mkdir(DIR_DATA_PATH)

if not os.path.exists(MEDIA_PATH):
    os.mkdir(MEDIA_PATH)

if not os.path.exists(STATIC_PATH):
    os.mkdir(STATIC_PATH)

if not os.path.exists(DIR_TEMPLATES_PATH):
    os.mkdir(DIR_TEMPLATES_PATH)

if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

if not os.path.isfile(FILE_CSV_PATH):
    with open(FILE_CSV_PATH, "w") as file:
        pass
