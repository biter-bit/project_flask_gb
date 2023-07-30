import os
from dotenv import load_dotenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg1234556"
    DEBUG = False
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    load_dotenv()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    WTF_CSRF_ENABLED = os.environ.get("WTF_CSRF_ENABLED")
    FLASK_ADMIN_SWATCH = os.environ.get('FLASK_ADMIN_SWATCH')
    OPENAPI_URL_PREFIX = os.environ.get('OPENAPI_URL_PREFIX')
    OPENAPI_SWAGGER_UI_PATH = os.environ.get('OPENAPI_SWAGGER_UI_PATH')
    OPENAPI_SWAGGER_UI_VERSION = os.environ.get('OPENAPI_SWAGGER_UI_VERSION')
