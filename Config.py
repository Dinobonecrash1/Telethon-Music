import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6263434715:AAEVzb0awAw8bgkKz1GooO0K2YV58KXUua0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJUBu8WPOsEG1J0w5FwBedLhm3CgzirBeCIOQe2VjANVIFUqrkOxZFDyP8ir0Trc4qbE2ivSBe61mGiaB4rF6r-evTwXYhkQ9ASG01XpZ2tgcpHLvHRnQqZgir1AmNmFC_8JWPVgDunEi9ZuCadyi9NcWGUzzh69aaHcgIT3zeK_hOqtQZBC6rWKhZVutmPSq7k3bJZj8P5ABnd6YAL6egbPSfFLTHqu8apXggoB6vRe81ss7XLiSj73mYZ0O0skp4i7LEpr7Dt5ZPbB-DYGlhRh0mNTN_pgREiCiYgLknNYXVsyvoRkJNZIT5sKYMuCU3-BvHQVxK2aCSGzhgedmt_wWSk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Nezukoooott_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
