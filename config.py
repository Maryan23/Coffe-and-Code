import os

class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    pass

config_options = {
   "production" :ProdConfig,
   'development' :DevConfig,
}