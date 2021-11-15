import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Mwiks01'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    

    #Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

    DEBUG = True


class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4543@localhost/coffeeandcode'
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    pass
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4543@localhost/coffeecode_test'

config_options = {
   "production" :ProdConfig,
   'development' :DevConfig,
   'test':TestConfig
}