import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4543@localhost/coffeeandcode'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Mwiks01'

    DEBUG = True

    #Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # MAIL_DEBUG = True
    MAIL_USERNAME = 'mwikali119@gmail.com'
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = 'mwikali119@gail.com'
    MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False


class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    pass
    DEBUG = True

config_options = {
   "production" :ProdConfig,
   'development' :DevConfig,
}