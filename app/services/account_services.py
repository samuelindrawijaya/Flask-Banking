import random
from app.models.account_models import Account
from app.config.connector import db
from datetime import datetime
class AccountServices:
    
    @staticmethod
    def get_all_accounts():
        return Account.query.filter_by(is_deleted=False).all()  
    
    @staticmethod
    def get_accounts_by_user(user_id):
        return Account.query.filter_by(user_id=user_id, is_deleted=False).all()  

    @staticmethod
    def get_account_by_id(account_id):
        account = Account.query.get(account_id)
        return account if account and not account.is_deleted else None 

    @staticmethod
    def create_account(user_id, account_type, balance=0):
        account = Account(
            user_id=user_id,
            account_type=account_type,
            account_number=str(random.randint(1000000000, 9999999999)),
            balance=balance,
            is_deleted=False  # Default
        )
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod


    def update_account(account_id, data):
        account = Account.query.get(account_id)
        if not account:
            return None  
        if 'account_number' in data:
            account.account_number = data['account_number']
        account.updated_at = datetime.utcnow()

        db.session.commit()
        return account


    @staticmethod
    def soft_delete_account(account_id):
        account = Account.query.get(account_id)
        account.is_deleted = True
        db.session.commit()
