"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from ...service import treatment_protocols_service
from ..general_controller import GeneralController


class Treatment_protocolsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = treatment_protocols_service
