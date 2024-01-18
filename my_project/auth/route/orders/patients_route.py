from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.patient_controller import PatientController

patient_bp = Blueprint('patient', __name__, url_prefix='/patient')
patient_controller = PatientController()

@patient_bp.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id: int) -> Response:
    return make_response(jsonify(patient_controller.get_patient_by_id(patient_id)), HTTPStatus.OK)

@patient_bp.route('', methods=['GET'])
def get_all_patients() -> Response:
    return make_response(jsonify(patient_controller.get_all_patients()), HTTPStatus.OK)

@patient_bp.route('', methods=['POST'])
def add_patient() -> Response:
    content = request.get_json()
    patient = Patient.create_from_dto(content)
    patient_controller.add_patient(patient)
    return make_response(jsonify(patient.put_into_dto()), HTTPStatus.CREATED)

@patient_bp.route('/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id: int) -> Response:
    content = request.get_json()
    patient = Patient.create_from_dto(content)
    patient_controller.update(patient_id, patient)
    return make_response("Patient updated", HTTPStatus.OK)

@patient_bp.route('/<int:patient_id>', methods=['PATCH'])
def patch_patient(patient_id: int) -> Response:
    content = request.get_json()
    patient_controller.patch(patient_id, content)
    return make_response("Patient updated", HTTPStatus.OK)

@patient_bp.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id: int) -> Response:
    patient_controller.delete(patient_id)
    return make_response("Patient deleted", HTTPStatus.OK)
