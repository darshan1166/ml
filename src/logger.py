import os
from datetime import datetime
import logging

LOG_FILE = f"{datetime.now()}.log"
LOG_PATH = os.path.join(os.getcwd(),"logs")
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

os.makedirs(LOG_PATH,exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("wassup biatch")