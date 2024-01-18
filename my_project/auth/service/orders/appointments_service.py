"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import appointments_dao
from ...service.general_service import GeneralService


class AppointmentsService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = appointments_dao
