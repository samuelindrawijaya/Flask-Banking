from app.utils.enum_type import ALLOWED_ACCOUNT_TYPES
from app.services.account_services import AccountServices
from app.utils.response import Response

class AccountValidator:

    @staticmethod
    def validate_account_creation(data, user_id):
        # Check if account type is valid
        if 'account_type' not in data or data['account_type'] not in ALLOWED_ACCOUNT_TYPES:
            return Response.error('Invalid account type. Allowed types: checking, savings, business', 400)
        # Ensure balance is not set when creating the account
        if 'balance' in data:
            return Response.error('Balance cannot be set during account creation', 400)
        
        if not user_id:
            return Response.error('Unauthorized access. Please log in first.', 403)
        return None

    @staticmethod
    def validate_account_update(data, account, user_id):
        # Check if account exists
        if not account:
            return Response.error('Account not found', 404)

        if account.user_id != user_id:
            return Response.error('Unauthorized access to this account', 403)
        
        if 'balance' in data:
            return Response.error('Balance cannot be changed during account update', 400)
        if 'account_type' in data:
            return Response.error('Account type cannot be changed during account update', 400)
        return None

    @staticmethod
    def validate_account_deletion(account, user_id):
        if not account:
            return Response.error('Account not found', 404)
        if account.user_id != user_id:
            return Response.error('Unauthorized access to this account', 403)
        return None

    @staticmethod
    def validate_account_ownership(account, user_id):
        if account.user_id != user_id:
            return Response.error('Unauthorized access to this account', 403)
        return None

