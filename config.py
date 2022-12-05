class Config:
    SECRET_KEY = 'mGAu6CAG9RTDd2np*'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='rober'
    MYSQL_PASSWORD=''
    MYSQL_DB='kokoro'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}