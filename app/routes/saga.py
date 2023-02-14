from DragonBall.Data import Sagas
import os

from flask import Blueprint, request, make_response, jsonify

base_name, file_extension = os.path.splitext(os.path.basename(__file__))
saga_blueprint = Blueprint('saga', __name__)


@saga_blueprint.route("/" + base_name + "/information" + "/<string:saga_name>")
def saga(saga_name):
    saga_name = Sagas.Sagas(saga_name).saga_information()
    return make_response(jsonify(saga_name), 200)


@saga_blueprint.route("/" + base_name + "/information-list", methods=["POST"])
def sagas():
    data_list = request.json.get("sagas", [])
    return make_response(jsonify(Sagas.Sagas.saga_list(data_list)), 200)


@saga_blueprint.route("/" + base_name + "/list")
def list_sagas():
    return Sagas.Sagas.list()
