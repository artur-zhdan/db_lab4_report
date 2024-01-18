from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
class AppointmentRecord(db.Model):
    __tablename__ = "appointment_records"

    record_id = db.Column(db.Integer, primary_key=True, nullable=False)
    record_datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"AppointmentRecord({self.record_id}, '{self.record_datetime}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "record_id": self.record_id,
            "record_datetime": str(self.record_datetime),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> AppointmentRecord:
        obj = AppointmentRecord(
            record_datetime=dto_dict.get("record_datetime"),
        )
        return obj
