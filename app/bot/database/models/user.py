import datetime
from typing import Literal

from beanie import Document


class User(Document):
    full_name: str
    telegram_id: int
    created_at: datetime
    post: Literal["admin", "support"]

    class Settings:
        name = "users"