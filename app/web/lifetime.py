from typing import Awaitable, Callable

from fastapi import FastAPI

from app.db.config import database


def startup(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """
    Actions to run on application startup.

    This function use fastAPI app to store data,
    such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    async def _startup() -> None:  # noqa: WPS430
        await database.connect()
        pass  # noqa: WPS420

    return _startup


def shutdown(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    async def _shutdown() -> None:  # noqa: WPS430
        await database.disconnect()
        pass  # noqa: WPS420

    return _shutdown
