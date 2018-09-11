import logging
from decouple import config

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
SEIFPI_JSON_URL = config('SEIFPI_JSON_URL')

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
