from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import AppointmentRecord, ScheduledVisit

class AppointmentRecordDAO(GeneralDAO):
    _domain_type = AppointmentRecord

    def get_scheduled_visits_for_record(self, record_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.record_id == record_id).all()
        return [visit.put_into_dto() for visit in visits]

    def get_records_by_date(self, record_date: str) -> list[AppointmentRecord]:
        session = self.get_session()
        records = session.query(AppointmentRecord).filter(AppointmentRecord.record_date == record_date).all()
        return [record.put_into_dto() for record in records]
