from decimal import Decimal
from app.services.transaction_services import TransactionService
from app.services.account_services import AccountServices
from flask import request
from flask_jwt_extended import get_jwt_identity
from app.utils.check_transaction import validate_transaction
from app.utils.response import Response
from flasgger import swag_from
from app.docs.transaction_swagger_specs import (
    get_all_transactions_admin_spec,
    get_all_transactions_spec,
    get_transaction_by_id_spec,
    create_transaction_spec
)

class TransactionController:

    @staticmethod
    @swag_from(get_all_transactions_admin_spec)
    def get_all_transactions_admin():
        transactions = TransactionService.get_all_transactions_admin()
        return Response.success([transaction.to_dict() for transaction in transactions], 200)

    @staticmethod
    @swag_from(get_all_transactions_spec)
    def get_all_transactions():
        user_id = get_jwt_identity()['user_id']
        accounts = AccountServices.get_accounts_by_user(user_id)
        account_ids = [account.id for account in accounts]
        transactions = TransactionService.get_transactions_by_user(account_ids)
        return Response.success([transaction.to_dict() for transaction in transactions], 200)

    @staticmethod
    @swag_from(get_transaction_by_id_spec)
    def get_transaction_by_id(transaction_id):
        transaction = TransactionService.get_transaction_by_id(transaction_id)
        if not transaction:
            return Response.error('Transaction not found', 404)
        user_id = get_jwt_identity()['user_id']
        if transaction.from_account.user_id != user_id and transaction.to_account.user_id != user_id:
            return Response.error('Unauthorized access', 403)
        return Response.success(transaction.to_dict(), 200)

    @staticmethod
    @swag_from(create_transaction_spec)
    def create_transaction():
        data = request.get_json()
        required_fields = ['from_account_id', 'amount', 'transaction_type']
        
       
        for field in required_fields:
            if field not in data or data[field] is None:
                return Response.error(f'{field} is required and cannot be null', 400)
        
        if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
            return Response.error('Invalid amount: Amount must be a positive number', 400)

        
        user_id = get_jwt_identity()['user_id']
        validator = validate_transaction(data, user_id)
        validation_error = validator.validate()
        if validation_error:
            return validation_error

        # Create transaction and return response
        transaction = TransactionService.create_transaction(data)
        return Response.success(transaction.to_dict(), 201)
