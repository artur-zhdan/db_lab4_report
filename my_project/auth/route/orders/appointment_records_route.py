from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.appointment_record_controller import AppointmentRecordController

appointment_record_bp = Blueprint('appointment_record', __name__, url_prefix='/appointment_record')
appointment_record_controller = AppointmentRecordController()

@appointment_record_bp.route('/<int:record_id>', methods=['GET'])
def get_appointment_record(record_id: int) -> Response:
    return make_response(jsonify(appointment_record_controller.get_appointment_record_by_id(record_id)), HTTPStatus.OK)

@appointment_record_bp.route('', methods=['GET'])
def get_all_appointment_records() -> Response:
    return make_response(jsonify(appointment_record_controller.get_all_appointment_records()), HTTPStatus.OK)

@appointment_record_bp.route('', methods=['POST'])
def add_appointment_record() -> Response:
    content = request.get_json()
    record = AppointmentRecord.create_from_dto(content)
    appointment_record_controller.add_appointment_record(record)
    return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)

@appointment_record_bp.route('/<int:record_id>', methods=['PUT'])
def update_appointment_record(record_id: int) -> Response:
    content = request.get_json()
    record = AppointmentRecord.create_from_dto(content)
    appointment_record_controller.update(record_id, record)
    return make_response("Appointment Record updated", HTTPStatus.OK)

@appointment_record_bp.route('/<int:record_id>', methods=['PATCH'])
def patch_appointment_record(record_id: int) -> Response:
    content = request.get_json()
    appointment_record_controller.patch(record_id, content)
    return make_response("Appointment Record updated", HTTPStatus.OK)

@appointment_record_bp.route('/<int:record_id>', methods=['DELETE'])
def delete_appointment_record(record_id: int) -> Response:
    appointment_record_controller.delete(record_id)
    return make_response("Appointment Record deleted", HTTPStatus.OK)
