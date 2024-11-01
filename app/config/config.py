import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://bankrevou_processget:2cab0c14bbafc777686c3a1dbb9514f6679d5adc@d27ig.h.filess.io:3307/bankrevou_processget?ssl_disabled=true"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    # MAIL SERVICE CONFIGURATION
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'clarisapp21@gmail.com'
    MAIL_PASSWORD = 'acdp ofua bjco xdrh'  
    MAIL_DEFAULT_SENDER = 'clarisapp21@gmail.com'
    