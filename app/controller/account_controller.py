from app.services.account_services import AccountServices
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from app.utils.validator_account import AccountValidator
from app.utils.response import Response
from flasgger import swag_from
from app.docs.account_swagger_specs import (
    get_all_accounts_admin_spec, 
    get_account_by_id_spec, 
    create_account_spec, 
    update_account_spec, 
    delete_account_spec,
    get_all_accounts_spec
)

class AccountController:

    @staticmethod
    @swag_from(get_all_accounts_spec)
    def get_all_accounts():
        user_id = get_jwt_identity()['user_id']
        accounts = AccountServices.get_accounts_by_user(user_id)
        return Response.success([account.to_dict() for account in accounts], 200)
    
    @staticmethod
    @swag_from(get_all_accounts_admin_spec)
    def get_all_accounts_admin():
        accounts = AccountServices.get_all_accounts()  # Fetch all active accounts from the database
        return Response.success([account.to_dict() for account in accounts], 200)
    
    @staticmethod
    @swag_from(get_account_by_id_spec)
    def get_account_by_id(account_id):
        account = AccountServices.get_account_by_id(account_id)
        user_id = get_jwt_identity()['user_id']
        if not account:
            return Response.error('Account not found', 404)
        validation_error = AccountValidator.validate_account_ownership(account, user_id)
        if validation_error:
            return validation_error
        return Response.success(account.to_dict(), 200)

    @staticmethod
    @swag_from(create_account_spec)
    def create_account():
        data = request.get_json()
        user_id = get_jwt_identity()['user_id']
        validation_error = AccountValidator.validate_account_creation(data, user_id)
        if validation_error:
            return validation_error

        account = AccountServices.create_account(user_id, data['account_type'], balance=0)
        return Response.success(account.to_dict(), 201)

    @staticmethod
    @swag_from(update_account_spec)
    def update_account(account_id):
        user_id = get_jwt_identity()['user_id']
        account = AccountServices.get_account_by_id(account_id)

        validation_error = AccountValidator.validate_account_update(request.get_json(), account, user_id)
        if validation_error:
            return validation_error

        updated_account = AccountServices.update_account(account_id, request.get_json())
        return Response.success(updated_account.to_dict(), 200)

    @staticmethod
    @swag_from(delete_account_spec)
    def delete_account(account_id):
        user_id = get_jwt_identity()['user_id']
        account = AccountServices.get_account_by_id(account_id)

        validation_error = AccountValidator.validate_account_deletion(account, user_id)
        if validation_error:
            return validation_error

        AccountServices.soft_delete_account(account_id)
        return Response.success({'message': 'Account marked as deleted successfully'}, 200)
