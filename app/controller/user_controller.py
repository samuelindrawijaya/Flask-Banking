from app.services.user_services import UserService
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from email_validator import validate_email, EmailNotValidError
from app.utils.response import Response

class UserController:
    
    @staticmethod
    def get_all_users_admin():
        """
        Get all users in the system for admin purposes.
        """
        users = UserService.get_all_users()
        return Response.success([user.to_dict() for user in users], 200)
    
    @staticmethod
    def add_user():
        data = request.get_json()

        # Validate email
        try:
            valid = validate_email(data['email'])  
            email = valid.email
        except EmailNotValidError as e:
            return Response.error(str(e), 400)

        # Get roles from request or assign default role ('User')
        roles = data.get('roles', ['User'])  

        # Create user
        user = UserService.create_user(data['username'], email, data['password'], roles)
        if not user:
            return Response.error('User could not be created, possibly due to duplicate email/username', 400)
        return Response.success(user.to_dict(), 201)

    @staticmethod
    def get_user_profile():
        user_id = get_jwt_identity()['user_id']
        user = UserService.get_user_by_id(user_id)
        if not user:
            return Response.error('User not found', 404)
        return Response.success(user.to_dict(), 200)

    @staticmethod
    def update_user_profile():
        user_id = get_jwt_identity()['user_id']
        data = request.get_json()

        # Validate email if provided using validate_email
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
