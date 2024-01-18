"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from ...service import appointment_records_service
from ..general_controller import GeneralController


class Appointment_recordsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = appointment_records_service
