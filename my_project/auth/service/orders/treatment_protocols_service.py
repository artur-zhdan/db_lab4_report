"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import treatment_protocols_dao
from ...service.general_service import GeneralService


class Treatment_protocolsService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = treatment_protocols_dao
