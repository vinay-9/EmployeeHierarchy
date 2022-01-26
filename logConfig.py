import logging
from logging.handlers import TimedRotatingFileHandler
import os

if os.path.exists("./log") == False:
    os.mkdir("./log")

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = TimedRotatingFileHandler("log/backend_log.log", when="midnight", interval=1)
handler.suffix = "%Y-%m-%d"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def logInfo(message):
    logger.info(message)


def logError(message):
    logger.error(message)
