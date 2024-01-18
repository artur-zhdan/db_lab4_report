from my_project.auth.dao.general_dao import GeneralDAO
from my_project.models import ConsultationCost, ScheduledVisit

class ConsultationCostDAO(GeneralDAO):
    _domain_type = ConsultationCost

    def get_scheduled_visits_for_cost(self, cost_id: int) -> list[ScheduledVisit]:
        session = self.get_session()
        visits = session.query(ScheduledVisit).filter(ScheduledVisit.cost_id == cost_id).all()
        return [visit.put_into_dto() for visit in visits]

    def get_costs_by_amount(self, amount: float) -> list[ConsultationCost]:
        session = self.get_session()
        costs = session.query(ConsultationCost).filter(ConsultationCost.amount == amount).all()
        return [cost.put_into_dto() for cost in costs]
