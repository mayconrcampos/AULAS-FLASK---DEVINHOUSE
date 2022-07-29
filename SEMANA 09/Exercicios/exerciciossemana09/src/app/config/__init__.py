from pickle import FALSE
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Development(object):
    DEBUG = True
    testing = False

class Production(object):
    DEBUG = False
    TESTING = False

app_config = {
    "development": Development,
    "production": Production
}