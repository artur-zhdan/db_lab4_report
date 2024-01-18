"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import appointments_service
from ..general_controller import GeneralController


class AppointmentsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = appointments_service
