"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from my_project import db

class Patient(db.Model):
    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Patient({self.patient_id}, '{self.first_name}', '{self.last_name}', '{self.address}', '{self.phone}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "phone": self.phone,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Patient:
        obj = Patient(
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            address=dto_dict.get("address"),
            phone=dto_dict.get("phone"),
        )
        return obj



