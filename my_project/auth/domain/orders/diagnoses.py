from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
class Diagnosis(db.Model):
    __tablename__ = "diagnoses"

    diagnosis_id = db.Column(db.Integer, primary_key=True, nullable=False)
    diagnosis = db.Column(db.String(50), nullable=False)
    diagnosis_date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Diagnosis({self.diagnosis_id}, '{self.diagnosis}', '{self.diagnosis_date}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "diagnosis_id": self.diagnosis_id,
            "diagnosis": self.diagnosis,
            "diagnosis_date": str(self.diagnosis_date),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> Diagnosis:
        obj = Diagnosis(
            diagnosis=dto_dict.get("diagnosis"),
            diagnosis_date=dto_dict.get("diagnosis_date"),
        )
        return obj
