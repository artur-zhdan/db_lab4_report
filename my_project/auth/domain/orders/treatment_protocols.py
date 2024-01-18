"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class TreatmentProtocol(db.Model):
    __tablename__ = "treatment_protocols"

    protocol_id = db.Column(db.Integer, primary_key=True, nullable=False)
    treatment_description = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"TreatmentProtocol({self.protocol_id}, '{self.treatment_description}', '{self.start_date}', '{self.end_date}')"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "protocol_id": self.protocol_id,
            "treatment_description": self.treatment_description,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> TreatmentProtocol:
        obj = TreatmentProtocol(
            treatment_description=dto_dict.get("treatment_description"),
            start_date=dto_dict.get("start_date"),
            end_date=dto_dict.get("end_date"),
        )
        return obj


