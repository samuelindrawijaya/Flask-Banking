from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.transaction_category_services import TransactionCategoryService
from app.utils.response import Response
from flasgger import swag_from
from app.docs.transaction_category_swagger_specs import (
    create_category_spec,
    get_all_categories_spec,
    get_category_by_id_spec,
    update_category_spec,
    delete_category_spec
)

class TransactionCategoryController:

    @staticmethod
    @swag_from(create_category_spec)
    @jwt_required()
    def create_category():
        data = request.get_json()
        if 'name' not in data or not data['name']:
            return Response.error("Category name is required", 400)
        
        category = TransactionCategoryService.create_category(data)
        return Response.success(category.to_dict(), 201)

    @staticmethod
    @swag_from(get_all_categories_spec)
    @jwt_required()
    def get_all_categories():
        categories = TransactionCategoryService.get_all_categories()
        return Response.success([category.to_dict() for category in categories], 200)

    @staticmethod
    @swag_from(get_category_by_id_spec)
    @jwt_required()
    def get_category_by_id(category_id):
        category = TransactionCategoryService.get_category_by_id(category_id)
        if not category:
            return Response.error("Category not found", 404)
        return Response.success(category.to_dict(), 200)

    @staticmethod
    @swag_from(update_category_spec)
    @jwt_required()
    def update_category(category_id):
        data = request.get_json()
        if 'name' not in data or not data['name']:
            return Response.error("Category name is required", 400)
        
        category = TransactionCategoryService.update_category(category_id, data)
        if not category:
            return Response.error("Category not found", 404)
        return Response.success(category.to_dict(), 200)

    @staticmethod
    @swag_from(delete_category_spec)
    @jwt_required()
    def delete_category(category_id):
        category = TransactionCategoryService.delete_category(category_id)
        if not category:
            return Response.error("Category not found", 404)
        return Response.success({"message": "Category deleted successfully"}, 200)
