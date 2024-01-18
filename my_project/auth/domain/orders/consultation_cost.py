"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class ConsultationCost(db.Model):
    __tablename__ = "consultation_cost"

    cost_id = db.Column(db.Integer, primary_key=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"ConsultationCost({self.cost_id}, {self.amount})"

    def put_into_dto(self) -> dict[str, object]:
        return {
            "cost_id": self.cost_id,
            "amount": self.amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, object]) -> ConsultationCost:
        obj = ConsultationCost(
            amount=dto_dict.get("amount"),
        )
        return obj

