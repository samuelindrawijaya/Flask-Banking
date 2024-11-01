from app.config.connector import db
from datetime import date

class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    biller_name = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('transactions_categories.id'), nullable=True)  # Add category link

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'biller_name': self.biller_name,
            'due_date': self.due_date.isoformat(),
            'amount': str(self.amount),
            'account_id': self.account_id,
            'category_id': self.category_id
        }

