import os
from typing import Literal

from dotenv import load_dotenv
from envparse import env

load_dotenv()

# a constant that stores some data
BOT_TOKEN: str = env.str("BOT_TOKEN")
MONGO_URI = os.environ.get('MONGO_URI', "mongodb://localhost:27017/prod")

available_llm_models: Literal['qwen2:7b-instruct-fp16'] = "qwen2:7b-instruct-fp16"
available_stt_models: Literal["base", "small"] = "small"
available_stt_languages: Literal["ru"] = "ru"

posts = Literal["admin", "moder", "support"]
super_user_id = 6898688536
