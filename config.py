from os import environ 

class Config:
    API_ID = environ.get("API_ID", "577678")
    API_HASH = environ.get("API_HASH", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
