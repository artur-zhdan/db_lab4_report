from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.consultation_cost_controller import ConsultationCostController

consultation_cost_bp = Blueprint('consultation_cost', __name__, url_prefix='/consultation_cost')
consultation_cost_controller = ConsultationCostController()

@consultation_cost_bp.route('/<int:cost_id>', methods=['GET'])
def get_consultation_cost(cost_id: int) -> Response:
    return make_response(jsonify(consultation_cost_controller.get_consultation_cost_by_id(cost_id)), HTTPStatus.OK)

@consultation_cost_bp.route('', methods=['GET'])
def get_all_consultation_costs() -> Response:
    return make_response(jsonify(consultation_cost_controller.get_all_consultation_costs()), HTTPStatus.OK)

@consultation_cost_bp.route('', methods=['POST'])
def add_consultation_cost() -> Response:
    content = request.get_json()
    cost = ConsultationCost.create_from_dto(content)
    consultation_cost_controller.add_consultation_cost(cost)
    return make_response(jsonify(cost.put_into_dto()), HTTPStatus.CREATED)

@consultation_cost_bp.route('/<int:cost_id>', methods=['PUT'])
def update_consultation_cost(cost_id: int) -> Response:
    content = request.get_json()
    cost = ConsultationCost.create_from_dto(content)
    consultation_cost_controller.update(cost_id, cost)
    return make_response("Consultation Cost updated", HTTPStatus.OK)

@consultation_cost_bp.route('/<int:cost_id>', methods=['PATCH'])
def patch_consultation_cost(cost_id: int) -> Response:
    content = request.get_json()
    consultation_cost_controller.patch(cost_id, content)
    return make_response("Consultation Cost updated", HTTPStatus.OK)

@consultation_cost_bp.route('/<int:cost_id>', methods=['DELETE'])
def delete_consultation_cost(cost_id: int) -> Response:
    consultation_cost_controller.delete(cost_id)
    return make_response("Consultation Cost deleted", HTTPStatus.OK)
