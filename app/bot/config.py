import os
from typing import Literal

from dotenv import load_dotenv
from envparse import env

load_dotenv()

# a constant that stores some data
BOT_TOKEN: str = env.str("BOT_TOKEN")
HF_TOKEN: str = env.str("HF_TOKEN")
MONGO_URI = os.environ.get('MONGO_URI', "mongodb://mongo_db:27017/prod")

available_llm_models: Literal['qwen2:7b-instruct-fp16'] = "qwen2:7b-instruct-fp16"
available_stt_models: Literal["base", "small"] = "small"
available_stt_languages: Literal["ru"] = "ru"

posts = ("admin", "moder", "support")
super_user_id = 6898688536
UPLOADS_DIR = '../../../uploads'
