from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import Appointment, ScheduledVisit

class AppointmentDAO(GeneralDAO):
    _domain_type = Appointment

    def get_scheduled_visits_for_appointment(self, appointment_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.appointment_id == appointment_id).all()
        return [visit.put_into_dto() for visit in visits]

    def get_appointments_for_doctor(self, doctor_id: int) -> list[Appointment]:
        session = self.get_session()
        appointments = session.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()
        return [appointment.put_into_dto() for appointment in appointments]
