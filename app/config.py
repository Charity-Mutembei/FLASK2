from Instance.config import MOVIE_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://newsapi.org/v2/everything/{}?api_key={}'

class ProdConfig (Config):
    '''
    Production configuration child class
    Args:
        Config: the parent configuration class with general configuration settings
    '''
    
class DevConfig(Config):
    '''
    Development configuration child class

    Args: 
        Config: the parent configuration class with general configuration settings
    '''

    DEBUG = True