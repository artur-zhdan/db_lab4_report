"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import appointment_records_dao
from ...service.general_service import GeneralService


class Appointment_recordsService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = appointment_records_dao
