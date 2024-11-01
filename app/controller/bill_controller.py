from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.bill_services import BillService
from app.utils.response import Response
from flasgger import swag_from
from app.docs.bill_swagger_specs import (
    create_bill_spec,
    get_all_bills_spec,
    update_bill_spec,
    delete_bill_spec,
    process_due_bills_spec
)

class BillController:

    @staticmethod
    @swag_from(create_bill_spec)
    def create_bill():
        user_id = get_jwt_identity()['user_id']
        data = request.get_json()
        
        required_fields = ['biller_name', 'due_date', 'amount', 'account_id']
        for field in required_fields:
            if field not in data or data[field] is None:
                return Response.error(f"{field} is required and cannot be null", 400)
        
        bill = BillService.create_bill(user_id, data)
        return Response.success(bill.to_dict(), 201)

    @staticmethod
    @swag_from(get_all_bills_spec)
    def get_all_bills():
        user_id = get_jwt_identity()['user_id']
        bills = BillService.get_bills_by_user(user_id)
        return Response.success([bill.to_dict() for bill in bills], 200)

    @staticmethod
    @swag_from(update_bill_spec)
    def update_bill(bill_id):
        data = request.get_json()
        bill = BillService.update_bill(bill_id, data)
        return Response.success(bill.to_dict(), 200)
    
    @staticmethod
    @swag_from(delete_bill_spec)
    def delete_bill(bill_id):
        BillService.delete_bill(bill_id)
        return Response.success({"message": "Bill deleted successfully"}, 200)

    @staticmethod
    @swag_from(process_due_bills_spec)
    def process_due_bills():
        BillService.process_due_bills()
        return Response.success({"message": "Due bills processed successfully"}, 200)
