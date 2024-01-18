from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import DoctorSchedule

class DoctorScheduleDAO(GeneralDAO):
    _domain_type = DoctorSchedule

    def get_doctor_schedules_for_doctor(self, doctor_id: int) -> list[DoctorSchedule]:
        session = self.get_session()
        schedules = session.query(DoctorSchedule).filter(DoctorSchedule.doctor_id == doctor_id).all()
        return [schedule.put_into_dto() for schedule in schedules]

    def get_doctor_schedules_by_day(self, day_of_week: str) -> list[DoctorSchedule]:
        session = self.get_session()
        schedules = session.query(DoctorSchedule).filter(DoctorSchedule.day_of_week == day_of_week).all()
        return [schedule.put_into_dto() for schedule in schedules]
