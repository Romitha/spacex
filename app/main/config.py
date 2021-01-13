import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    # configuration of mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'algewatta.developer@gmail.com'
    MAIL_PASSWORD = 'tviawaschurbgkwt'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    CORS_ALLOW_HEADERS = True
    CORS_EXPOSE_HEADERS = True
    CORS_HEADERS = 'Content-Type'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(user='root',
                                                                                                    password='Janith@0771818404',
                                                                                                    server='34.87.118.229',
                                                                                                    database='spacex')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'xchenage.io'
    SECURITY_PASSWORD_SALT = 'my_precious_two'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
