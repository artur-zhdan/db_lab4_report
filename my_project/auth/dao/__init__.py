"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
# from .orders.client_dao import ClientDAO
# from .orders.client_type_dao import ClientTypeDAO

from .orders.appointments_dao import  AppointmentDAO
from .orders.doctor_dao import DoctorDAO
from .orders.patients_dao import PatientDAO
from .orders.doctor_schedules_dao import DoctorScheduleDAO
from .orders.consultation_cost_dao import ConsultationCostDAO
from .orders.treatment_protocols_dao import TreatmentProtocolDAO
from .orders.diagnoses_dao import DiagnosisDAO
from .orders.appointment_records_dao import AppointmentRecordDAO

appointments_dao = AppointmentDAO()
doctor_dao = DoctorDAO()
patients_dao = PatientDAO()
doctor_schedules_dao = DoctorScheduleDAO()
consultation_cost_dao = ConsultationCostDAO()
treatment_protocols_dao = TreatmentProtocolDAO()
diagnoses_dao = DiagnosisDAO()
appointment_records_dao = AppointmentRecordDAO ()

