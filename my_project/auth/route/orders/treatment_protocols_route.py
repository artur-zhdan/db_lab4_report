from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.treatment_protocol_controller import TreatmentProtocolController

treatment_protocol_bp = Blueprint('treatment_protocol', __name__, url_prefix='/treatment_protocol')
treatment_protocol_controller = TreatmentProtocolController()

@treatment_protocol_bp.route('/<int:protocol_id>', methods=['GET'])
def get_treatment_protocol(protocol_id: int) -> Response:
    return make_response(jsonify(treatment_protocol_controller.get_treatment_protocol_by_id(protocol_id)), HTTPStatus.OK)

@treatment_protocol_bp.route('', methods=['GET'])
def get_all_treatment_protocols() -> Response:
    return make_response(jsonify(treatment_protocol_controller.get_all_treatment_protocols()), HTTPStatus.OK)

@treatment_protocol_bp.route('', methods=['POST'])
def add_treatment_protocol() -> Response:
    content = request.get_json()
    protocol = TreatmentProtocol.create_from_dto(content)
    treatment_protocol_controller.add_treatment_protocol(protocol)
    return make_response(jsonify(protocol.put_into_dto()), HTTPStatus.CREATED)

@treatment_protocol_bp.route('/<int:protocol_id>', methods=['PUT'])
def update_treatment_protocol(protocol_id: int) -> Response:
    content = request.get_json()
    protocol = TreatmentProtocol.create_from_dto(content)
    treatment_protocol_controller.update(protocol_id, protocol)
    return make_response("Treatment Protocol updated", HTTPStatus.OK)

@treatment_protocol_bp.route('/<int:protocol_id>', methods=['PATCH'])
def patch_treatment_protocol(protocol_id: int) -> Response:
    content = request.get_json()
    treatment_protocol_controller.patch(protocol_id, content)
    return make_response("Treatment Protocol updated", HTTPStatus.OK)

@treatment_protocol_bp.route('/<int:protocol_id>', methods=['DELETE'])
def delete_treatment_protocol(protocol_id: int) -> Response:
    treatment_protocol_controller.delete(protocol_id)
    return make_response("Treatment Protocol deleted", HTTPStatus.OK)
