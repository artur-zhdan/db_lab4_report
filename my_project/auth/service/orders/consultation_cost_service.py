"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...dao.orders import consultation_cost_dao
from ...service.general_service import GeneralService


class Consultation_costService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = consultation_cost_dao
