from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import Patient, AppointmentRecord, ScheduledVisit

class PatientDAO(GeneralDAO):
    _domain_type = Patient

    def get_appointment_records_for_patient(self, patient_id: int) -> list[AppointmentRecord]:
        session = self.get_session()
        records = session.query(AppointmentRecord).filter(AppointmentRecord.patient_id == patient_id).all()
        return [record.put_into_dto() for record in records]

    def get_scheduled_visits_for_patient(self, patient_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.patient_id == patient_id).all()
        return [visit.put_into_dto() for visit in visits]
