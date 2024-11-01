from app.utils.enum_type import ALLOWED_TRANSACTION_TYPES
from app.utils.response import Response
from datetime import datetime, timedelta
from decimal import Decimal
from app.services.account_services import AccountServices
from app.services.transaction_services import TransactionService
from app.services.budget_services import BudgetService
from app.utils.transaction_rules import get_transaction_rules
from app.models.budget_models import Budget

def validate_transaction(data, user_id):
    from_account = AccountServices.get_account_by_id(data['from_account_id'])
    if not from_account:
        return Response.error("Source account does not exist", 400)

    # Only check `to_account` if a `to_account_id` is provided (i.e., for transfers)
    if data.get('to_account_id'):
        to_account = AccountServices.get_account_by_id(data['to_account_id'])
        if not to_account:
            return Response.error("Destination account does not exist", 400)
    transaction_type = data['transaction_type']
    
    # Retrieve rules for the account type and validate transaction type
    rules = get_transaction_rules(from_account.account_type)
    if not rules:
        return Response.error(f"No rules defined for account type: {from_account.account_type}", 400)
    if transaction_type not in rules['allowed_transactions']:
        return Response.error(f"{transaction_type.capitalize()} transactions are not allowed for {from_account.account_type}", 400)
    
    # Ownership and account-specific checks
    if from_account.user_id != user_id:
        return Response.error('Unauthorized: You do not own this account', 403)
    if transaction_type in ['withdrawal', 'transfer'] and from_account.balance < Decimal(data['amount']):
        return Response.error('Insufficient funds for the transaction', 400)
    
    # Daily and monthly transaction limits
    daily_total = TransactionService.get_daily_transaction_total(from_account.id)
    monthly_total = TransactionService.get_monthly_transaction_total(from_account.id)
    if daily_total + Decimal(data['amount']) > rules['daily_limit']:
        return Response.error('Daily transaction limit exceeded', 400)
    if monthly_total + Decimal(data['amount']) > rules['monthly_limit']:
        return Response.error('Monthly transaction limit exceeded', 400)
    
    # Hold period validation for withdrawals and transfers
    hold_period = rules.get('hold_period', timedelta(0))
    last_deposit_time = from_account.last_deposit_time
    if transaction_type in ["withdrawal", "transfer"] and last_deposit_time:
        if datetime.now() - last_deposit_time < hold_period:
            return Response.error('Funds on hold; transaction not allowed', 400)

    # Specific rules for transaction types
    if transaction_type == 'deposit' and 'to_account_id' in data and data['to_account_id'] is not None:
        return Response.error('Invalid transaction: Deposit should not have a to_account_id', 400)
    if transaction_type == 'withdrawal' and 'to_account_id' in data and data['to_account_id'] is not None:
        return Response.error('Invalid transaction: Withdrawal should not have a to_account_id', 400)
    if transaction_type == 'transfer' and data['to_account_id'] == data['from_account_id']:
        return Response.error('Transfer requires different source and destination accounts', 400)
    if 'bill_id' in data and transaction_type != 'bill payment':
        return Response.error('Invalid transaction type for a bill payment', 400)

    # Budget validation for category-based tracking
    if rules.get("budget_tracking") and data.get('category_id'):
        budget = Budget.query.filter_by(category_id=data['category_id'], user_id=user_id).first()
        if budget:
            new_total_spent = budget.total_spent + Decimal(data['amount'])
            if new_total_spent > budget.amount:
                return Response.error(f"Warning: This transaction will exceed your budget for category {budget.name}.", 400)
            # BudgetService.update_spending(budget.id, Decimal(data['amount']))

    return None  # Passes validation
