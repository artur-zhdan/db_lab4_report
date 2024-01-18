"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.appointment_route import appointment_bp
    from .orders.patients_route import patient_bp
    from .orders.doctor_route import doctor_bp
    from .orders.diagnoses_route import diagnosis_bp
    from .orders.doctor_schedules_route import doctor_schedule_bp
    from .orders.appointment_records_route import appointment_record_bp
    from .orders.consultation_cost_route import consultation_cost_bp
    from .orders.treatment_protocols_route import treatment_protocol_bp

    app.register_blueprint(appointment_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(diagnosis_bp)
    app.register_blueprint(doctor_schedule_bp)
    app.register_blueprint(appointment_record_bp)
    app.register_blueprint(consultation_cost_bp)
    app.register_blueprint(treatment_protocol_bp)
