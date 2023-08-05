import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29377368")) #optional
API_HASH = getenv("API_HASH", "55a61ddfeb88e75e95de3005598cfa9c") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "1428445604"))
MONGO_URL = getenv("MONGO_URL" ,"mongodb+srv://jepof32886:J3EoSIoVg5lDfdsy@cluster0.u5tize5.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCxIilLQzG63fkOAIj1LKL9iVoaO4PyfD9JEqDzfLLnPlRItb4tXPSd4NQMmKlkkc5zhDT43T6zPi8hXhy_wT0O2BDeh5cvP1Lk44U302eP2bjUujnMawn67jQYQL7XaRqEQL1wNkyhNjCB_T4iwLamt0h44vU88yiLt77UD7tq2H3KCDmYrE_psyKqW_HIMZNqlxcYY5NcXZ6yUBSz5BB566MiSlEnEtSiAI5y5gfal0_rbYjNpYkWqZKizxz4qCBOtzbNlF6Oh8oT9mmKytjtkcgHd_xb4ezvHt_fYf3EiZaJNujdodMA9zmXPnso8vQrfK15RpyXqDKboY6Nn9VSRZpAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
