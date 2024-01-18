"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import consultation_cost_service
from ..general_controller import GeneralController


class Consultation_costController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = consultation_cost_service
