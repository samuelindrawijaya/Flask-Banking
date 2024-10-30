from app.models.user_role_models import User, Role  # Import Role model
from sqlalchemy.exc import IntegrityError
from app.config.connector import db

class UserService:
    @staticmethod
    def create_user(username, email, password, roles=None):
        try:
            # Create a new User object
            user = User(username=username, email=email)
            user.set_password(password)  # Hash the password before storing it
            if roles:
                for role_name in roles:
                    role = Role.query.filter_by(name=role_name).first()
                    if role:
                        user.roles.append(role)  
                    else:
                        return None  
            else:
                # If no roles are provided, assign the default role 'User'
                default_role = Role.query.filter_by(name='User').first()
                if default_role:
                    user.roles.append(default_role)
                else:
                    return None  # Handle missing default role scenario

            
            db.session.add(user)
            db.session.commit()
            return user 
        except IntegrityError:
            db.session.rollback()
            return None  # Handle unique constraint violations (duplicate email, username)

    @staticmethod
    def get_user_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, username=None, email=None, password=None, roles=None):
        try:
            user = db.session.get(User, user_id)
            if user:
                # Update fields if they are provided
                if username:
                    user.username = username
                if email:
                    user.email = email
                if password:
                    user.set_password(password)  
                    
                if roles:
                    user.roles.clear()  
                    for role_name in roles:
                        role = Role.query.filter_by(name=role_name).first()
                        if role:
                            user.roles.append(role)

                db.session.commit()  
            return user 
        except IntegrityError:
            db.session.rollback()
            return None  # Handle unique constraint violations (duplicate email, username)
