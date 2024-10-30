from app.models.account_models import Account
from app.models.transaction_models import Transaction
from app.config.connector import db

class TransactionService:
    
    @staticmethod
    def get_all_transactions_admin():
        return Transaction.query.all()
    
    @staticmethod
    def get_transactions_by_user(account_ids):
        return Transaction.query.filter(
            Transaction.from_account_id.in_(account_ids) | 
            Transaction.to_account_id.in_(account_ids)
        ).all()

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.query.get(transaction_id)

    @staticmethod
    def create_transaction(data):
        transaction = Transaction(
            from_account_id=data['from_account_id'],
            to_account_id=data.get('to_account_id'),  # Only for transfers
            amount=data['amount'],
            transaction_type=data['transaction_type'],
            description=data.get('description')
        )

        from_account = Account.query.get(data['from_account_id'])
        if data['transaction_type'] == 'deposit':
            from_account.balance += data['amount']
        elif data['transaction_type'] == 'withdrawal':
            if from_account.balance < data['amount']:
                raise ValueError('Insufficient funds for withdrawal')
            from_account.balance -= data['amount']
        elif data['transaction_type'] == 'transfer':
            if from_account.balance < data['amount']:
                raise ValueError('Insufficient funds for transfer')
            from_account.balance -= data['amount']

            to_account = Account.query.get(data['to_account_id'])
            to_account.balance += data['amount']
            
        db.session.add(transaction)
        db.session.commit()
        return transaction
