"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import diagnoses_dao
from ...service.general_service import GeneralService


class DiagnosesService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = diagnoses_dao
