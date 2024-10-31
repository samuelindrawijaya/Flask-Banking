import datetime
import pyotp  # For 2FA
from flask import jsonify, request
from app.config.connector import db
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    get_jwt_identity, 
    jwt_required
)
from app.services.user_services import UserService
from app.utils.response import Response
from flask_mail import Message
from app import mail
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import swag_from
from app.docs.auth_swagger_specs import (
    login_spec, 
    verify_2fa_spec, 
    logout_spec, 
    enable_2fa_spec, 
    refresh_token_spec
)

class AuthController:
    
    @staticmethod
    @swag_from(login_spec)
    def login():
        
        data = request.get_json()

        # Check if email is provided
        if 'email' not in data or not data['email']:
            return Response.error("Email is required", 400)
        
        # Check if password is provided
        if 'password' not in data or not data['password']:
            return Response.error("Password is required", 400)

        user = UserService.get_user_by_email(data['email'])
        if not user:
            return Response.error("Invalid email", 401)
        if not check_password_hash(user.password_hash, data['password']):
            return Response.error("Invalid password", 401)

        access_token = create_access_token(
            identity={'user_id': user.id, 'role': user.roles[0].name},  # Assuming roles exist
            expires_delta=datetime.timedelta(hours=1)  # Token expiry time
        )
        refresh_token = create_refresh_token(identity={'user_id': user.id})

        if user.two_factor_secret:
            return Response.success({
                'message': '2FA enabled, please verify the OTP',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200)

        return Response.success({
            'message': 'Logged in successfully',
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200)

    @staticmethod
    @swag_from(verify_2fa_spec)
    def verify_2fa():
        data = request.get_json()
        user_id = get_jwt_identity()['user_id']
        user = UserService.get_user_by_id(user_id)

        if not user.two_factor_secret:
            return Response.error('2FA not enabled for this user', 400)

        provided_otp = data['otp_code']

        totp = pyotp.TOTP(user.two_factor_secret)
        current_otp = totp.now()  # Generate OTP on the server
        print(f"Current OTP (on server): {current_otp}")
        print(f"User's 2FA Secret: {user.two_factor_secret}")

        if totp.verify(provided_otp, valid_window=1):
            user.two_factor_verified = True
            db.session.commit()
            return Response.success({"message": "2FA verified successfully"}, 200)
        else:
            return Response.error("Invalid 2FA code", 400)


    @staticmethod
    @swag_from(logout_spec)
    def logout():
        user_id = get_jwt_identity()['user_id']
        user = UserService.get_user_by_id(user_id)
        user.two_factor_verified = False  # Reset 2FA verification on logout
        db.session.commit()

        return Response.success({'message': 'Logged out successfully'}, 200)

    @staticmethod
    @swag_from(enable_2fa_spec)
    def enable_2fa():
        user_id = get_jwt_identity()['user_id']
        user = UserService.get_user_by_id(user_id)
        
        secret = pyotp.random_base32()  
        user.two_factor_secret = secret
        db.session.commit()  

        # Generate a provisioning URI (for Google Authenticator, etc.)
        otp_provisioning_url = pyotp.totp.TOTP(secret).provisioning_uri(
            user.email, issuer_name="Revou Bank"
        )

        totp = pyotp.TOTP(secret)
        current_otp = totp.now()
        try:
            msg = Message(
                subject="Enable 2FA for Your Account",
                recipients=[user.email],
                body=f"Revou Bank Authenticator\n\n"
                     f"Or use this secret key: {current_otp}"
            )
            mail.send(msg)

            return Response.success({"message": "2FA enabled and setup email sent"}, 200)
        except Exception as e:
            return Response.error(f"Error sending email: {str(e)}", 500)

    @staticmethod
    @swag_from(refresh_token_spec)
    @jwt_required(refresh=True)
    def refresh_token():
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        return Response.success({
            "access_token": new_access_token
        }, 200)



