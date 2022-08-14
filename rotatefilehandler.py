import logging
import time
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=1000, backupCount=3)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('RotatingFileHandler   Hi Hi')
    time.sleep(5)