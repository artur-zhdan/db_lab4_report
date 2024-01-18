"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.doctor_controller import DoctorController
from .orders.diagnoses_controller import DiagnosesController
from .orders.patients_controller import PatientsController
from .orders.appointments_controller import AppointmentsController
from .orders.appointment_records_controller import Appointment_recordsController
from .orders.consultation_cost_controller import Consultation_costController
from .orders.doctor_schedules_controller import Doctor_schedulesController
from .orders.treatment_protocols_controller import Treatment_protocolsController


doctor_controller = DoctorController()
diagnoses_controller = DiagnosesController()
patients_controller = PatientsController()
appointments_controller = AppointmentsController()
appointment_records_controller = Appointment_recordsController()
consultation_cost_controller = Consultation_costController()
doctor_schedules_controller = Doctor_schedulesController()
treatment_protocols_controller = Treatment_protocolsController()