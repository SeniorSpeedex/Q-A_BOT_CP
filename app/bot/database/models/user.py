from datetime import datetime

from beanie import Document, Indexed

from enum import Enum

class PostEnum(str, Enum):
    admin = "admin"
    moder = "moder"
    support = "support"

class User(Document):
    full_name: str
    telegram_id: Indexed(int, unique=True)
    created_at: datetime
    post: PostEnum

    class Settings:
        name = "users"

