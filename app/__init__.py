from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import config
import os

def register_blueprint(app : Flask):
    from .view.child import child_blueprint
    app.register_blueprint(child_blueprint)

    from .view.parents import parents_blueprint
    app.register_blueprint(parents_blueprint)

    from .view.user import user_blueprint
    app.register_blueprint(user_blueprint)

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "12341234213"
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    login_manager = LoginManager()
    login_manager.init_app(app)

    db = SQLAlchemy(app)

    register_blueprint(app)

    return app