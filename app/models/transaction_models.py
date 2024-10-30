from datetime import datetime, timezone
from app.config.connector import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    from_account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    to_account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_type = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships with explicit overlaps to resolve conflicts
    from_account = db.relationship('Account', back_populates='transactions_from', foreign_keys=[from_account_id])

    # Many Transactions belong to One Account (to_account)
    to_account = db.relationship('Account', back_populates='transactions_to', foreign_keys=[to_account_id])
    
    def to_dict(self):
        return {
            'id': self.id,
            'from_account_id': self.from_account_id,
            'to_account_id': self.to_account_id,
            'amount': str(self.amount),
            'transaction_type': self.transaction_type,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }
