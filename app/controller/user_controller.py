# user_controller.py
from app.services.user_services import UserService
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from email_validator import validate_email, EmailNotValidError
from app.utils.response import Response
from flasgger import swag_from
from app.docs.user_swagger_specs import (
    get_all_users_admin_spec,
    add_user_spec,
    get_user_profile_spec,
    update_user_profile_spec
)

class UserController:
    
    @staticmethod
    @swag_from(get_all_users_admin_spec)
    def get_all_users_admin():
        users = UserService.get_all_users()
        return Response.success([user.to_dict() for user in users], 200)
    
    @staticmethod
    @swag_from(add_user_spec)
    def add_user():
        data = request.get_json()

        try:
            valid = validate_email(data['email'])  
            email = valid.email
        except EmailNotValidError as e:
            return Response.error(str(e), 400)

        roles = data.get('roles', ['User'])  
        user = UserService.create_user(data['username'], email, data['password'], roles)
        if not user:
            return Response.error('User could not be created, possibly due to duplicate email/username', 400)
        return Response.success(user.to_dict(), 201)

    @staticmethod
    @swag_from(get_user_profile_spec)
    def get_user_profile():
        user_id = get_jwt_identity()['user_id']
        user = UserService.get_user_by_id(user_id)
        if not user:
            return Response.error('User not found', 404)
        return Response.success(user.to_dict(), 200)

    @staticmethod
    @swag_from(update_user_profile_spec)
    def update_user_profile():
        user_id = get_jwt_identity()['user_id']
        data = request.get_json()

        if 'email' in data:
            try:
                valid = validate_email(data['email'])
                data['email'] = valid.email
            except EmailNotValidError as e:
                return Response.error(str(e), 400)

        roles = data.get('roles')
        user = UserService.update_user(user_id, data.get('username'), data.get('email'), data.get('password'), roles)
        
        if not user:
            return Response.error('User not found or update failed', 404)
        return Response.success(user.to_dict(), 200)
