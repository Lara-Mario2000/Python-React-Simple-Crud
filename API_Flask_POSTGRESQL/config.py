class Config:
    DATABASE_URL = 'postgres://mario:hfsjikArkUFr9bG0yTfLtJtAMByT1ogN@dpg-ck902hk7m7is73bse410-a.oregon-postgres.render.com/simple_crud_i2wl'

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}
