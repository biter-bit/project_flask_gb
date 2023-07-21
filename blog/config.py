import os
from dotenv import load_dotenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg1234556"
    DEBUG = False


class DevConfig(BaseConfig):
    load_dotenv()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    WTF_CSRF_ENABLED = os.environ.get("WTF_CSRF_ENABLED")
