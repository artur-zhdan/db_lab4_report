"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import doctor_schedules_dao
from ...service.general_service import GeneralService


class Doctor_schedulesService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = doctor_schedules_dao
