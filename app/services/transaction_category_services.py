from app.models.transaction_category_models import TransactionCategory
from app.config.connector import db

class TransactionCategoryService:
    
    @staticmethod
    def create_category(data):
        category = TransactionCategory(name=data['name'])
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def get_all_categories():
        return TransactionCategory.query.all()
    
    @staticmethod
    def get_category_by_id(category_id):
        return TransactionCategory.query.get(category_id)
    
    @staticmethod
    def update_category(category_id, data):
        category = TransactionCategory.query.get(category_id)
        if not category:
            return None
        category.name = data['name']
        db.session.commit()
        return category
    
    @staticmethod
    def delete_category(category_id):
        category = TransactionCategory.query.get(category_id)
        if not category:
            return None
        db.session.delete(category)
        db.session.commit()
        return category
