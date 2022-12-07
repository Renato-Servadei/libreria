
from decouple import config
class Config:
    SECRET_KEY = 'mGAu6CAG9RTDd2np*'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='rober'
    MYSQL_PASSWORD=''
    MYSQL_DB='kokoro'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jaycipetela@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}