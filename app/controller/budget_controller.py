from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.services.budget_services import BudgetService
from app.utils.response import Response
from flasgger import swag_from
from app.docs.budget_swagger_specs import (
    create_budget_spec,
    get_all_budgets_spec,
    update_budget_spec
)

class BudgetController:

    @staticmethod
    @swag_from(create_budget_spec)
    def create_budget():
        user_id = get_jwt_identity()['user_id']
        data = request.get_json()
        
        required_fields = ['name', 'amount', 'start_date', 'end_date', 'category_id']
        for field in required_fields:
            if field not in data or data[field] is None:
                return Response.error(f"{field} is required and cannot be null", 400)

        budget = BudgetService.create_budget(user_id, data)
        return Response.success(budget.to_dict(), 201)

    @staticmethod
    @swag_from(get_all_budgets_spec)
    def get_all_budgets():
        user_id = get_jwt_identity()['user_id']
        budgets = BudgetService.get_budgets_by_user(user_id)
        return Response.success([budget.to_dict() for budget in budgets], 200)

    @staticmethod
    @swag_from(update_budget_spec)
    def update_budget(budget_id):
        data = request.get_json()
        budget = BudgetService.update_budget(budget_id, data)
        return Response.success(budget.to_dict(), 200)
