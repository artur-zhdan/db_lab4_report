from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import TreatmentProtocol, ScheduledVisit

class TreatmentProtocolDAO(GeneralDAO):
    _domain_type = TreatmentProtocol

    def get_scheduled_visits_for_protocol(self, protocol_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.protocol_id == protocol_id).all()
        return [visit.put_into_dto() for visit in visits]

    def get_protocols_by_start_date(self, start_date: str) -> list[TreatmentProtocol]:
        session = self.get_session()
        protocols = session.query(TreatmentProtocol).filter(TreatmentProtocol.start_date == start_date).all()
        return [protocol.put_into_dto() for protocol in protocols]
