"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import patients_dao
from ...service.general_service import GeneralService


class PatientsService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = patients_dao
