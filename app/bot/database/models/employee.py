from datetime import datetime

from beanie import Document, Indexed

from enum import Enum

from pydantic import Field


class PostEnum(str, Enum):
    admin = "admin"
    moder = "moder"
    support = "support"

class Employee(Document):
    full_name: str
    telegram_id: Indexed(int, unique=True)
    created_at: datetime = Field(default=datetime.now())
    post: PostEnum

    class Settings:
        name = "users"

