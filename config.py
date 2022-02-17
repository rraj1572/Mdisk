import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5215557666:AAE3HndfHYX3hasN0sNtaa-eBr_NBXL9_yc")

    API_ID = int(os.environ.get("API_ID", 13823924))

    API_HASH = os.environ.get("API_HASH", "fc9ff0358a79ce0db532703417955721")
    
    API_KEY = os.environ.get("API_KEY", "rzhQb7R9Jj505KWZwW7G")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))
