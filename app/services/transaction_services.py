from datetime import datetime
from sqlalchemy import func
from decimal import Decimal
from app.models.account_models import Account
from app.models.transaction_models import Transaction
from app.models.budget_models import Budget
from app.config.connector import db
from app.services.budget_services import BudgetService

class TransactionService:
    
    @staticmethod
    def get_all_transactions_admin():
        return Transaction.query.all()
    
    @staticmethod
    def get_transactions_by_user(account_ids):
        return Transaction.query.filter(
            (Transaction.from_account_id.in_(account_ids)) | 
            (Transaction.to_account_id.in_(account_ids))
        ).all()
        
    @staticmethod
    def get_daily_transaction_total(account_id):
        """Get the total transaction amount for an account for the current day."""
        today = datetime.now().date()
        daily_total = (
            db.session.query(func.sum(Transaction.amount))
            .filter(
                Transaction.from_account_id == account_id,
                func.date(Transaction.created_at) == today
            )
            .scalar()
        )
        return daily_total or 0

    @staticmethod
    def get_monthly_transaction_total(account_id):
        """Get the total transaction amount for an account for the current month."""
        first_day_of_month = datetime.now().replace(day=1)
        monthly_total = (
            db.session.query(func.sum(Transaction.amount))
            .filter(
                Transaction.from_account_id == account_id,
                Transaction.created_at >= first_day_of_month
            )
            .scalar()
        )
        return monthly_total or 0

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.query.get(transaction_id)

    @staticmethod
    def create_transaction(data):
        transaction = Transaction(
            from_account_id=data['from_account_id'],
            to_account_id=data.get('to_account_id'),
            amount=Decimal(data['amount']),
            transaction_type=data['transaction_type'],
            description=data.get('description'),
            category_id=data.get('category_id'),  # For budget tracking
            bill_id=data.get('bill_id')  # For bill payments
        )

        from_account = Account.query.get(data['from_account_id'])
        if not from_account:
            raise ValueError("Source account not found")

        # Process transaction based on type
        if data['transaction_type'] == 'deposit':
            from_account.balance += transaction.amount
            from_account.last_deposit_time = datetime.now()
        
        elif data['transaction_type'] == 'withdrawal':
            if from_account.balance < transaction.amount:
                raise ValueError('Insufficient funds for withdrawal')
            from_account.balance -= transaction.amount
        
        elif data['transaction_type'] == 'transfer':
            to_account = Account.query.get(data['to_account_id'])
            if not to_account:
                raise ValueError('Destination account not found')
            if from_account.balance < transaction.amount:
                raise ValueError('Insufficient funds for transfer')
            from_account.balance -= transaction.amount
            to_account.balance += transaction.amount

        elif data['transaction_type'] == 'bill payment':
            if from_account.balance < transaction.amount:
                raise ValueError('Insufficient funds for bill payment')
            from_account.balance -= transaction.amount

        # Update Budget if category_id is present
        if data.get('category_id'):
            budget = Budget.query.filter_by(category_id=data['category_id'], user_id=from_account.user_id).first()
            if budget:
                new_total_spent = budget.total_spent + transaction.amount
                if new_total_spent > budget.amount:
                    print(f"Warning: This transaction exceeds the budget for category {budget.name}.")
                BudgetService.update_spending(budget.id, transaction.amount)

        # Commit transaction
        db.session.add(transaction)
        db.session.commit()
        return transaction
