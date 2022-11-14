from bot.config import (
    client,
    logger,
    IMAGE_URL,
    PHOTOS_PATH as PATH,
    TIME_INTERVAL,
    REMOVE_FORMER_PHOTO,
)
from telethon.tl.functions.photos import (
    DeletePhotosRequest,
    UploadProfilePhotoRequest,
)
from telethon.tl.types import InputPhoto

import aiofiles
import aiohttp
import asyncio


"""
async def _long_sleep(delay: int) -> None:
    hours = 60 * 60  # 60 * 60 = 3600 seconds in 1 hour

    async def _bg() -> None:
        while True:
            await asyncio.sleep(12 * hours)

    task = asyncio.create_task(_bg())
    try:
        await asyncio.sleep(delay)
    finally:
        task.cancel()
"""


async def delete_former_photo() -> None:
    """
    Delete outdated photos.
    """
    try:
        photo: InputPhoto = (await client.get_profile_photos("me"))[1]
        await client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=photo.id,
                        access_hash=photo.access_hash,
                        file_reference=photo.file_reference,
                    )
                ]
            )
        )
        logger.info("successful photo deletion")
    except Exception as ex:
        logger.error(ex)


async def download_image(source: str) -> str:
    """
    Download photo from image-generator site.
    """
    async with aiohttp.ClientSession() as session:
        response: aiohttp.ClientResponse = await session.get(source, ssl=False)
        if response.status != 200:
            raise Exception(response.status, response.text)
        async with aiofiles.open(".tmp.jpg", mode="wb") as file:
            async for data in response.content.iter_any():
                await file.write(data)
            return str(file.name)


async def update_photo_from_remote(url: str) -> None:
    """
    Update Profile Photo.
    """
    try:
        image_path: str = await download_image(url)
        await client(
            UploadProfilePhotoRequest(await client.upload_file(image_path))
        )
        logger.info("successful photo updation")
    except Exception as ex:
        logger.error(ex)


async def update_photo_from_local(path: str) -> None:
    """
    Update Profile Photo.
    """
    try:
        await client(UploadProfilePhotoRequest(await client.upload_file(path)))
        logger.info("successful photo updation")
    except FileNotFoundError:
        logger.warning("pictures are over")
        raise IndexError
    except Exception as ex:
        logger.error(ex)


async def main() -> None:
    """
    Main function to call other public functions.
    """
    count = 0
    while True:
        try:
            # await update_photo_from_local(PATH + "/" + str(count) + ".jpg")
            await update_photo_from_remote(IMAGE_URL)
            if REMOVE_FORMER_PHOTO is True:
                await delete_former_photo()
            await asyncio.sleep(TIME_INTERVAL)
            count += 1
        except IndexError:
            count = 0


if __name__ == "__main__":
    try:
        logger.info("BOT STARTED")
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("BOT STOPPED")
    except Exception as ex:
        logger.error(ex)
