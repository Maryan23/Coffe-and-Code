import os

class Config:
    '''
    General configuration parent class
    '''
    pass  
    DEBUG = True

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