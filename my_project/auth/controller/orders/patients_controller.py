"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import patients_service
from ..general_controller import GeneralController


class PatientsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = patients_service
