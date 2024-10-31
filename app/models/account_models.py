from datetime import datetime, timezone
from app.config.connector import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    account_type = db.Column(db.String(255), nullable=False)
    account_number = db.Column(db.String(255), unique=True, nullable=False)
    balance = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    # Define the relationships with explicit overlaps
    transactions_from = db.relationship('Transaction', foreign_keys='Transaction.from_account_id', back_populates='from_account')
    transactions_to = db.relationship('Transaction', foreign_keys='Transaction.to_account_id', back_populates='to_account')

    def to_dict(self):
        return {
            'id': self.id,
            'account_type': self.account_type,
            'account_number': self.account_number,
            'balance': str(self.balance),
            'created_at': self.created_at.isoformat(),
            'transactions': [transaction.to_dict() for transaction in self.transactions_from + self.transactions_to]
        }
