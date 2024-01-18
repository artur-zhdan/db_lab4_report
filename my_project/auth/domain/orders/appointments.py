from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
class Appointment(db.Model):
    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    appointment_datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"Appointment({self.appointment_id}, '{self.appointment_datetime}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "appointment_id": self.appointment_id,
            "appointment_datetime": str(self.appointment_datetime),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Appointment:
        obj = Appointment(
            appointment_datetime=dto_dict.get("appointment_datetime"),
        )
        return obj
