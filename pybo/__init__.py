#pip flask, flask-migrate, flask-sqlalchemy, flask-wtf

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM init
    db.init_app(app)
    migrate.init_app(app, db)

    # DB init
    from . import models

    # Flask View
    from .views import main_views, user_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)   # /
    app.register_blueprint(user_views.bp)   # /user
    app.register_blueprint(question_views.bp)  # question
    app.register_blueprint(answer_views.bp) # answer
    app.register_blueprint(auth_views.bp) # auth

    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app