import os

API_ID = int(os.environ.get("API_ID", "27836929"))
API_HASH = os.environ.get("API_HASH", "e6a8edbb6dc21865e2ac7d98525e601d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7650081375:AAFzBJO7rxVD5pNMDglUEPDI_rSk5i-abO0")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1002056408106")
IS_PRIVATE = os.environ.get("IS_PRIVATE" ,"True") # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "6221524623"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', "-1001901787276")
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
