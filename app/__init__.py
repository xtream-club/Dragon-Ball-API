from flask import Flask
from app.routes.character import character_blueprint
from app.routes.saga import saga_blueprint
from app.routes.planet import planet_blueprint
from app.routes.fusion import fusion_blueprint
from app.routes.videogame import game_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(character_blueprint)
    app.register_blueprint(saga_blueprint)
    app.register_blueprint(planet_blueprint)
    app.register_blueprint(fusion_blueprint)
    app.register_blueprint(game_blueprint)

    return app
