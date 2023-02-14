from flask import Flask, jsonify
from app.routes.character import character_blueprint
from app.routes.saga import saga_blueprint
from app.routes.planeta import planet_blueprint
from app.routes.fusion import fusion_blueprint
from app.routes.videogame import game_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

data_info = {"character": "/character/information/name", "planet": "/planet/information/name",
             "saga": "/saga/information/name", "fusion": "/fusion/information/name",
             "game": "/videogame/information/name"}


@app.route("/")
def home():
    return jsonify(data_info)


if __name__ == '__main__':
    app.register_blueprint(character_blueprint)
    app.register_blueprint(saga_blueprint)
    app.register_blueprint(planet_blueprint)
    app.register_blueprint(fusion_blueprint)
    app.register_blueprint(game_blueprint)
    app.run()
