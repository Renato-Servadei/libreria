class Config:
    SECRET_KEY = 'mGAu6CAG9RTDd2np*'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}