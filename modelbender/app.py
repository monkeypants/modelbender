from flask import Flask

from modelbender.rest import domain
from modelbender.flask_settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(domain.blueprint)
    return app
