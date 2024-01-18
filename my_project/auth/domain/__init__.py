"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
import sys
# # add path to sys.path
# sys.path.append('/Users/arturzhdan/uni/s3/db/app')
# from my_project.auth.domain.orders. import Client
# from .auth.domain.orders.client_type import ClientType

"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.doctor import Doctor
from .orders.diagnoses import Diagnosis
from .orders.patients import Patient
from .orders.appointments import Appointment
from .orders.appointment_records import AppointmentRecord
from .orders.consultation_cost import ConsultationCost
from .orders.doctor_schedules import DoctorSchedule
from .orders.treatment_protocols import TreatmentProtocol


doctor = Doctor()
diagnoses = Diagnosis()
patients = Patient()
appointments = Appointment()
appointment_records = AppointmentRecord()
consultation_cost = ConsultationCost()
doctor_schedules = DoctorSchedule()
treatment_protocols = TreatmentProtocol()

