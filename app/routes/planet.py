from DragonBall.Data import Planets
import os

from flask import Blueprint, request, make_response, jsonify

base_name, file_extension = os.path.splitext(os.path.basename(__file__))
planet_blueprint = Blueprint('planets', __name__)


@planet_blueprint.route("/" + base_name + "/information" + "/<string:planet_name>")
def planet(planet_name):
    planet_name = Planets.Planets(planet_name).planet_information()
    return make_response(jsonify(planet_name), 200)


@planet_blueprint.route("/" + base_name + "/information-list", methods=["POST"])
def planets():
    data_list = request.json.get("planets", [])
    return make_response(jsonify(Planets.Planets.planet_list(data_list)), 200)


@planet_blueprint.route("/" + base_name + "/list")
def list_planets():
    return Planets.Planets.list()
