class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:password@localhost/pitchit'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True