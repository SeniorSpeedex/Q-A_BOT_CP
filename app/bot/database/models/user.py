import datetime
from typing import Literal

from beanie import Document, Indexed

from app.bot.config import posts


class User(Document):
    full_name: str
    telegram_id: Indexed(int, unique=True)
    created_at: datetime
    post: posts



    class Settings:
        name = "users"