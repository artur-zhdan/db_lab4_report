from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.orders.controllers.doctor_schedule_controller import DoctorScheduleController

doctor_schedule_bp = Blueprint('doctor_schedule', __name__, url_prefix='/doctor_schedule')
doctor_schedule_controller = DoctorScheduleController()

@doctor_schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_doctor_schedule(schedule_id: int) -> Response:
    return make_response(jsonify(doctor_schedule_controller.get_doctor_schedule_by_id(schedule_id)), HTTPStatus.OK)

@doctor_schedule_bp.route('', methods=['GET'])
def get_all_doctor_schedules() -> Response:
    return make_response(jsonify(doctor_schedule_controller.get_all_doctor_schedules()), HTTPStatus.OK)

@doctor_schedule_bp.route('', methods=['POST'])
def add_doctor_schedule() -> Response:
    content = request.get_json()
    schedule = DoctorSchedule.create_from_dto(content)
    doctor_schedule_controller.add_doctor_schedule(schedule)
    return make_response(jsonify(schedule.put_into_dto()), HTTPStatus.CREATED)

@doctor_schedule_bp.route('/<int:schedule_id>', methods=['PUT'])
def update_doctor_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    schedule = DoctorSchedule.create_from_dto(content)
    doctor_schedule_controller.update(schedule_id, schedule)
    return make_response("Doctor Schedule updated", HTTPStatus.OK)

@doctor_schedule_bp.route('/<int:schedule_id>', methods=['PATCH'])
def patch_doctor_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    doctor_schedule_controller.patch(schedule_id, content)
    return make_response("Doctor Schedule updated", HTTPStatus.OK)

@doctor_schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
def delete_doctor_schedule(schedule_id: int) -> Response:
    doctor_schedule_controller.delete(schedule_id)
    return make_response("Doctor Schedule deleted", HTTPStatus.OK)
