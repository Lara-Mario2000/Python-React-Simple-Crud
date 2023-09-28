class Config:
    DATABASE_URL = 'DATABASE_URL'

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}
