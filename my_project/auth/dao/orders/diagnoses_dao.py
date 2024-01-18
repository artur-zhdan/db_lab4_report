from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import Diagnosis, ScheduledVisit

class DiagnosisDAO(GeneralDAO):
    _domain_type = Diagnosis

    def get_scheduled_visits_for_diagnosis(self, diagnosis_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.diagnosis_id == diagnosis_id).all()
        return [visit.put_into_dto() for visit in visits]

    def get_diagnoses_by_date(self, diagnosis_date: str) -> list[Diagnosis]:
        session = self.get_session()
        diagnoses = session.query(Diagnosis).filter(Diagnosis.diagnosis_date == diagnosis_date).all()
        return [diagnosis.put_into_dto() for diagnosis in diagnoses]
