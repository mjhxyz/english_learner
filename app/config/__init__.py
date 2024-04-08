class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:000000@192.168.60.128:3306/english_learner'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    pass
