from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from clinic.doctor.controller import doctor_controller

doctor_bp = Blueprint('doctor', __name__, url_prefix='/clinic/doctors')

@doctor_bp.get('/<int:doctor_id>')
def get_doctor(doctor_id: int) -> Response:
    return make_response(jsonify(doctor_controller.find_by_id(doctor_id)), HTTPStatus.OK)

@doctor_bp.get('')
def get_all_doctors() -> Response:
    return make_response(jsonify(doctor_controller.find_all()), HTTPStatus.OK)

@doctor_bp.post('')
def create_doctor() -> Response:
    content = request.get_json()
    obj = Doctor.create_from_dto(content)  # Assuming Doctor class with create_from_dto method
    doctor_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)

@doctor_bp.put('/<int:doctor_id>')
def update_doctor(doctor_id: int) -> Response:
    content = request.get_json()
    obj = Doctor.create_from_dto(content)
    doctor_controller.update(doctor_id, obj)
    return make_response("Doctor updated", HTTPStatus.OK)

@doctor_bp.patch('/<int:doctor_id>')
def patch_doctor(doctor_id: int) -> Response:
    content = request.get_json()
    doctor_controller.patch(doctor_id, content)
    return make_response("Doctor updated", HTTPStatus.OK)

@doctor_bp.delete('/<int:doctor_id>')
def delete_doctor(doctor_id: int) -> Response:
    doctor_controller.delete(doctor_id)
    return make_response("Doctor deleted", HTTPStatus.OK)
