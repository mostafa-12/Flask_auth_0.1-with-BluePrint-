import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class BaseConfig:
    DEBUG = True
    SECRET_KEY = "VERY SECRET KEY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass
