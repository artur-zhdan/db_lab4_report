"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import doctor_schedules_service
from ..general_controller import GeneralController


class Doctor_schedulesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = doctor_schedules_service
