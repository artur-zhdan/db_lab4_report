"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import doctor_dao
from ...service.general_service import GeneralService


class DoctorService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = doctor_dao
