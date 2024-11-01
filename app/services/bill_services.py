from flask_jwt_extended import get_jwt_identity
from app.models.account_models import Account
from app.models.bill_models import Bill
from app.config.connector import db
from datetime import date
from decimal import Decimal

from app.models.budget_models import Budget
from app.models.transaction_models import Transaction

class BillService:

    @staticmethod
    def create_bill(user_id, data):
        bill = Bill(user_id=user_id, **data)
        db.session.add(bill)
        db.session.commit()
        return bill

    @staticmethod
    def get_bills_by_user(user_id):
        return Bill.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_bill(bill_id, data):
        bill = Bill.query.get(bill_id)
        for key, value in data.items():
            setattr(bill, key, value)
        db.session.commit()
        return bill

    @staticmethod
    def delete_bill(bill_id):
        bill = Bill.query.get(bill_id)
        db.session.delete(bill)
        db.session.commit()

    @staticmethod
    def process_due_bills():
        user_id = get_jwt_identity()['user_id']
        today = date.today()

        due_bills = Bill.query.filter_by(due_date=today, user_id=user_id).all()
        print(due_bills)
        for bill in due_bills:
            account = Account.query.get(bill.account_id)
            if account and account.user_id == user_id and account.balance >= bill.amount:
                account.balance -= Decimal(bill.amount)

                transaction = Transaction(
                    from_account_id=bill.account_id,
                    amount=bill.amount,
                    transaction_type="bill payment",
                    bill_id=bill.id
                )
                
                db.session.add(transaction)
            
                budget = Budget.query.filter_by(category_id=bill.category_id, user_id=user_id).first()
                if budget:
                    budget.total_spent += bill.amount
                    if budget.total_spent > budget.amount:
                        print(f"Warning: Budget exceeded for category {budget.name}")
                        
                db.session.commit()
            else:
                print(f"Insufficient funds for bill ID {bill.id} or unauthorized access. Payment could not be processed.")
