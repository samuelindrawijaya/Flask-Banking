from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from app.config.connector import db, migrate, jwt,mail  # Import extensions
from app.config.config import Config
# from app.models.userRoleModel import User
# from app.seeds.seeds import seed_data
from flasgger import Swagger

from app.seed.seeds import seed_data

def create_app():
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    
    Swagger(app, 
    template={
            "swagger": "2.0",
            "info": {
                "title": "Revou Bank API",
                "description": "Revou Bank API made by Flask and MySQL",
                "contact": {
                "responsibleOrganization": "ME",
                "responsibleDeveloper": "Me",
                "email": "me@me.com",
                "url": "www.me.com",
                }
            },
            "securityDefinitions": {
                "bearerAuth": {
                    "type": "apiKey",
                    "name": "Authorization",
                    "in": "header",
                    "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
                }
            },
            "security": [
                {"bearerAuth": []}
            ],
        }
    )
    
    # Register Blueprints
    from app.routes.api_routes import user_bp, account_bp, transaction_bp, auth_bp, role_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(account_bp, url_prefix='/api/accounts')
    app.register_blueprint(transaction_bp, url_prefix='/api/transactions')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(role_bp, url_prefix='/api/roles')
    
    # Define basic routes for DB creation and seeding
    @app.route('/')
    def index():
        return 'hello'
    
    @app.route('/create-all-db')
    def create_all_db():
        db.create_all()  # No need to return anything here
        return 'Database tables created successfully!'
    
    @app.route('/create-all-seed')
    def create_seed():
        seed_data()
        return 'Database seeded successfully!'
    return app
