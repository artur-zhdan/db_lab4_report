from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.appointments_controller import AppointmentController
appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')
appointment_controller = AppointmentController()

@appointment_bp.route('/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id: int) -> Response:
    return make_response(jsonify(appointment_controller.get_appointment_by_id(appointment_id)), HTTPStatus.OK)

@appointment_bp.route('', methods=['GET'])
def get_all_appointments() -> Response:
    return make_response(jsonify(appointment_controller.get_all_appointments()), HTTPStatus.OK)

@appointment_bp.route('', methods=['POST'])
def add_appointment() -> Response:
    content = request.get_json()
    appointment = Appointment.create_from_dto(content)
    appointment_controller.add_appointment(appointment)
    return make_response(jsonify(appointment.put_into_dto()), HTTPStatus.CREATED)

@appointment_bp.route('/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id: int) -> Response:
    content = request.get_json()
    appointment = Appointment.create_from_dto(content)
    appointment_controller.update(appointment_id, appointment)
    return make_response("Appointment updated", HTTPStatus.OK)

@appointment_bp.route('/<int:appointment_id>', methods=['PATCH'])
def patch_appointment(appointment_id: int) -> Response:
    content = request.get_json()
    appointment_controller.patch(appointment_id, content)
    return make_response("Appointment updated", HTTPStatus.OK)

@appointment_bp.route('/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id: int) -> Response:
    appointment_controller.delete(appointment_id)
    return make_response("Appointment deleted", HTTPStatus.OK)
