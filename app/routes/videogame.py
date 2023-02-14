from DragonBall.Data import VideoGames
import os

from flask import Blueprint, request, make_response, jsonify

base_name, file_extension = os.path.splitext(os.path.basename(__file__))
game_blueprint = Blueprint('game', __name__)


@game_blueprint.route("/" + base_name + "/information" + "/<string:game_name>")
def saga(game_name):
    game_name = VideoGames.VideoGames(game_name).game_information()
    return make_response(jsonify(game_name), 200)


@game_blueprint.route("/" + base_name + "/information-list", methods=["POST"])
def sagas():
    data_list = request.json.get("games", [])
    return make_response(jsonify(VideoGames.VideoGames.game_list(data_list)), 200)


@game_blueprint.route("/" + base_name + "/list")
def list_sagas():
    return VideoGames.VideoGames.list()
