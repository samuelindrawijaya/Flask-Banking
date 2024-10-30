from app.config.connector import db
from app.models.user_role_models import Role, User

def seed_roles():
    """
    Seed the database with initial roles.
    """
    roles = ['Admin', 'User']
    for role_name in roles:
        existing_role = Role.query.filter_by(name=role_name).first()
        if not existing_role:
            role = Role(name=role_name)
            db.session.add(role)
    db.session.commit()
    print("Roles seeded successfully.")

def seed_user():
    """
    Seed the database with an initial admin user.
    """
    # Check if user already exists
    existing_user = User.query.filter_by(email='admin@example.com').first()
    if not existing_user:
        admin_role = Role.query.filter_by(name='Admin').first()
        if not admin_role:
            print("Admin role does not exist. Please seed roles first.")
            return
        
        user = User(
            username='admin',
            email='admin@example.com'
        )
        user.set_password('adminpassword')  # Securely hash the password
        user.roles.append(admin_role)  # Assign the admin role to this user
        db.session.add(user)
        db.session.commit()
        print("Admin user seeded successfully.")
    else:
        print("Admin user already exists.")

def seed_data():
    """
    Seed both roles and the initial user.
    """
    seed_roles()
    seed_user()
