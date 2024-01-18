from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import Doctor, DoctorSchedule

class DoctorDAO(GeneralDAO):
    _domain_type = Doctor

    def get_schedules_for_doctor(self, doctor_id: int) -> list[DoctorSchedule]:
        session = self.get_session()
        schedules = session.query(DoctorSchedule).filter(DoctorSchedule.doctor_id == doctor_id).all()
        return [schedule.put_into_dto() for schedule in schedules]

    def get_doctor_by_specialty(self, specialty: str) -> list[Doctor]:
        session = self.get_session()
        doctors = session.query(Doctor).filter(Doctor.specialty == specialty).all()
        return [doctor.put_into_dto() for doctor in doctors]
