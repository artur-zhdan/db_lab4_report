"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import diagnoses_service
from ..general_controller import GeneralController


class DiagnosesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = diagnoses_service
