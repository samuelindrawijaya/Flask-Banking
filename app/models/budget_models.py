from app.config.connector import db
from datetime import date

class Budget(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('transactions_categories.id'), nullable=False)  # Updated here
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    start_date = db.Column(db.Date, default=date.today)
    end_date = db.Column(db.Date, nullable=False)
    total_spent = db.Column(db.Numeric(10, 2), default=0.00)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'name': self.name,
            'amount': str(self.amount),
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'total_spent': str(self.total_spent)
        }
