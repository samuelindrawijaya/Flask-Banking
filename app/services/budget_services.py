from app.models.budget_models import Budget
from app.config.connector import db

class BudgetService:

    @staticmethod
    def create_budget(user_id, data):
        budget = Budget(user_id=user_id, **data)
        db.session.add(budget)
        db.session.commit()
        return budget

    @staticmethod
    def get_budgets_by_user(user_id):
        return Budget.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_budget(budget_id, data):
        budget = Budget.query.get(budget_id)
        for key, value in data.items():
            setattr(budget, key, value)
        db.session.commit()
        return budget

    @staticmethod
    def update_spending(budget_id, transaction_amount):
        budget = Budget.query.get(budget_id)
        budget.total_spent += transaction_amount
        if budget.total_spent > budget.amount:
            print(f"Warning: Budget for {budget.name} exceeded!")
        db.session.commit()
        return budget
