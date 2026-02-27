from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import BaseConfig
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"
from .models import User
from .main import main
from .auth import auth
def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    BaseConfig.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        user = User.query.get(int(user_id))
        return user
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
