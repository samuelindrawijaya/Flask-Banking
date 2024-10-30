from app.services.account_services import AccountServices
from app.utils.enum_type import ALLOWED_TRANSACTION_TYPES
from app.utils.response import Response


def validate_transaction(data, user_id):
    
    if data['transaction_type'] not in ALLOWED_TRANSACTION_TYPES:
            return Response.error('Invalid transaction type. Allowed types: deposit, withdrawal, transfer', 400)
        
    from_account = AccountServices.get_account_by_id(data['from_account_id'])
    if not from_account:
        return Response.error('From account not found', 404)
    
    to_account = AccountServices.get_account_by_id(data['to_account_id'])
    if not to_account:
        return Response.error('to account not found', 404)
        
    if from_account.user_id != user_id:
        return Response.error('Unauthorized: You do not own this account', 403)

    if data['transaction_type'] == 'deposit':
        if data['to_account_id'] != data['from_account_id']: 
            return Response.error('Invalid transaction: Deposit transactions must use the same account for both fields.', 400)
        
    if data['transaction_type'] == 'deposit':
        if data['to_account_id'] != data['from_account_id']: 
            return Response.error('Invalid transaction: Deposit transactions must use the same account for both fields.', 400)
    
    elif data['transaction_type'] == 'withdrawal':
        if data['to_account_id'] != data['from_account_id']: 
            return Response.error('Invalid transaction: withdrawal transactions must use the same account for both fields.', 400)
        if from_account.balance < data['amount']:
            return Response.error('Insufficient funds for withdrawal', 400)
         
    elif data['transaction_type'] == 'transfer':
            if from_account.account_type == 'savings' and to_account.account_type == 'savings':
                return Response.error('Transfers are not allowed to or from savings accounts', 400)
            if 'to_account_id' not in data:
                return Response.error('Transfer requires a to_account_id', 400)
            if data['to_account_id'] == data['from_account_id']:
                return Response.error('Transfer transaction must have different source and destination accounts', 400)
            if from_account.balance < data['amount']:
                return Response.error('Insufficient funds for transfer', 400)