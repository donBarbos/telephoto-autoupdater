from colorama import Fore
from dotenv import load_dotenv
from loguru import logger
from telethon import TelegramClient

import colorama
import os


def set_name_of_photos(path: str) -> None:
    """
    Renames all photos from 0 to N, where N - number of photos.
    """
    files = os.listdir(path)
    files = [file for file in files if os.path.isfile(path + "/" + file)]
    for index, image_file in enumerate(files):
        os.rename(
            os.path.join(path + "/" + image_file),
            os.path.join(path + "/" + str(index) + ".jpg"),
        )


def set_var(var_name: str) -> str:
    """
    Called until the user enters a value for the variable.
    """
    result: str | None = (
        os.getenv(var_name)
        if os.getenv(var_name)
        else input(f"${var_name} is empty, enter the value: ")
    )
    if not result:
        print(Fore.RED + "Incorrect input!")
        result: str | None = set_var(var_name)
    return result


colorama.init(autoreset=True)
load_dotenv()
NAME: str = set_var("NAME")
API_ID: int = int(set_var("API_ID"))
API_HASH: str = set_var("API_HASH")
IMAGE_URL: str = set_var("IMAGE_URL")
PHOTOS_PATH: str = set_var("PHOTOS_PATH")
TIME_INTERVAL: int = int(set_var("TIME_INTERVAL")) * 60 * 60
REMOVE_FORMER_PHOTO: bool = bool(int(set_var("REMOVE_FORMER_PHOTO")))

set_name_of_photos(PHOTOS_PATH)
client = TelegramClient(NAME, API_ID, API_HASH)

logger.add(
    "logs/bot.log",
    level="DEBUG",
    format="{time} | {level} | {module}:{function}:{line} | {message}",
    rotation="100 KB",
    compression="zip",
)
