"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class DoctorSchedule(db.Model):
    __tablename__ = "doctor_schedules"

    schedule_id = db.Column(db.Integer, primary_key=True, nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    def __repr__(self) -> str:
        return f"DoctorSchedule({self.schedule_id}, '{self.day_of_week}', '{self.start_time}', '{self.end_time}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "schedule_id": self.schedule_id,
            "day_of_week": self.day_of_week,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> DoctorSchedule:
        obj = DoctorSchedule(
            day_of_week=dto_dict.get("day_of_week"),
            start_time=dto_dict.get("start_time"),
            end_time=dto_dict.get("end_time"),
        )
        return obj

