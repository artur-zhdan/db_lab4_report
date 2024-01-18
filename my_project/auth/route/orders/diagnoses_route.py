from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.diagnosis_controller import DiagnosisController

diagnosis_bp = Blueprint('diagnosis', __name__, url_prefix='/diagnosis')
diagnosis_controller = DiagnosisController()

@diagnosis_bp.route('/<int:diagnosis_id>', methods=['GET'])
def get_diagnosis(diagnosis_id: int) -> Response:
    return make_response(jsonify(diagnosis_controller.get_diagnosis_by_id(diagnosis_id)), HTTPStatus.OK)

@diagnosis_bp.route('', methods=['GET'])
def get_all_diagnoses() -> Response:
    return make_response(jsonify(diagnosis_controller.get_all_diagnoses()), HTTPStatus.OK)

@diagnosis_bp.route('', methods=['POST'])
def add_diagnosis() -> Response:
    content = request.get_json()
    diagnosis = Diagnosis.create_from_dto(content)
    diagnosis_controller.add_diagnosis(diagnosis)
    return make_response(jsonify(diagnosis.put_into_dto()), HTTPStatus.CREATED)

@diagnosis_bp.route('/<int:diagnosis_id>', methods=['PUT'])
def update_diagnosis(diagnosis_id: int) -> Response:
    content = request.get_json()
    diagnosis = Diagnosis.create_from_dto(content)
    diagnosis_controller.update(diagnosis_id, diagnosis)
    return make_response("Diagnosis updated", HTTPStatus.OK)

@diagnosis_bp.route('/<int:diagnosis_id>', methods=['PATCH'])
def patch_diagnosis(diagnosis_id: int) -> Response:
    content = request.get_json()
    diagnosis_controller.patch(diagnosis_id, content)
    return make_response("Diagnosis updated", HTTPStatus.OK)

@diagnosis_bp.route('/<int:diagnosis_id>', methods=['DELETE'])
def delete_diagnosis(diagnosis_id: int) -> Response:
    diagnosis_controller.delete(diagnosis_id)
    return make_response("Diagnosis deleted", HTTPStatus.OK)
