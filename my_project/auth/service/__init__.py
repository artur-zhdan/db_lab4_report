"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.doctor_service import DoctorService
from .orders.diagnoses_service import DiagnosesService
from .orders.patients_service import PatientsService
from .orders.appointments_service import AppointmentsService
from .orders.appointment_records_service import Appointment_recordsService
from .orders.consultation_cost_service import Consultation_costService
from .orders.doctor_schedules_service import Doctor_schedulesService
from .orders.treatment_protocols_service import Treatment_protocolsService


doctor_service = DoctorService()
diagnoses_service = DiagnosesService()
patients_service = PatientsService()
appointments_service = AppointmentsService()
appointment_records_service = Appointment_recordsService()
consultation_cost_service = Consultation_costService()
doctor_schedules_service = Doctor_schedulesService()
treatment_protocols_service = Treatment_protocolsService()
