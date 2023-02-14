from DragonBall.Data import Characters
import os

from flask import Blueprint, request, make_response, jsonify

base_name, file_extension = os.path.splitext(os.path.basename(__file__))
character_blueprint = Blueprint('character', __name__)


@character_blueprint.route("/" + base_name + "/information" + "/<string:character_name>")
def character(character_name):
    character_name = Characters.Characters(character_name).character_information()
    return make_response(jsonify(character_name), 200)


@character_blueprint.route("/" + base_name + "/information-list", methods=["POST"])
def characters():
    data_list = request.json.get("characters", [])
    return make_response(jsonify(Characters.Characters.character_list(data_list)), 200)


@character_blueprint.route("/" + base_name + "/list")
def list_characters():
    return Characters.Characters.list()