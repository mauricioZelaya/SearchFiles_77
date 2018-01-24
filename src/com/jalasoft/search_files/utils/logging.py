"""
This module is the logger
"""

import logging.config
from definition import CONFIG_PATH

logging.config.fileConfig(CONFIG_PATH)
LOGGER = logging.getLogger('SearchFiles')
