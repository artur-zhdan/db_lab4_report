"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

# /my_project/__init__.py
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Doctor(db.Model):
    __tablename__ = "doctors"

    doctor_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(50), nullable=False)
    license_number = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Doctor({self.doctor_id}, '{self.first_name}', '{self.last_name}', '{self.specialty}', '{self.license_number}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "doctor_id": self.doctor_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "specialty": self.specialty,
            "license_number": self.license_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Doctor:
        obj = Doctor(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            specialty=dto_dict.get("specialty"),
            license_number=dto_dict.get("license_number"),
        )
        return obj

