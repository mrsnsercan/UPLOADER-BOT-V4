import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6306109430:AAFgPH0959ni7yU747Yn_1f-jqW2mCW-0Y0")
    
    API_ID = int(os.environ.get("API_ID", "28772700"))
    
    API_HASH = os.environ.get("API_HASH", "8fcb8d4edf60fd44316701dd239eeb13")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "1")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001918456384"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001918456384")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5054973867"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@xxtabixbot")
                                  
