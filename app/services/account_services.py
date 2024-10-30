import random
from app.models.account_models import Account
from app.config.connector import db

class AccountServices:
    
    @staticmethod
    def get_all_accounts():
        return Account.query.all() 
    
    @staticmethod
    def get_accounts_by_user(user_id):
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_account_by_id(account_id):
        return Account.query.get(account_id)

    @staticmethod
    def create_account(user_id, account_type, balance):
        account = Account(user_id=user_id, account_type=account_type, account_number=random.randint(1000000000, 9999999999), balance=balance)
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def update_account(account_id, data):
        account = Account.query.get(account_id)
        if 'account_type' in data:
            account.account_type = data['account_type']
        if 'balance' in data:
            account.balance = data['balance']
        db.session.commit()
        return account

    @staticmethod
    def delete_account(account_id):
        account = Account.query.get(account_id)
        db.session.delete(account)
        db.session.commit()
