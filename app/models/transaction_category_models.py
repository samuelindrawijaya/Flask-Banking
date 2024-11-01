from datetime import datetime
from app.config.connector import db
class TransactionCategory(db.Model):
    __tablename__ = 'transactions_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }