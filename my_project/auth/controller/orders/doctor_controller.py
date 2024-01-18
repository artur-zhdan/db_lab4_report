"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import doctor_service
from ..general_controller import GeneralController


class DoctorController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = doctor_service
