"""
This file contains the config reader class.

:author: guylev38
:date: 26/12/2025
"""

# ----- Imports ----- #

import os
import logging
from pathlib import Path

from dotenv import load_dotenv

from models.config import Config

# ----- Classes ----- #

class MissingConfigField(BaseException):
    pass

class ConfigReader:
    @staticmethod
    def read_config() -> Config:
        load_dotenv()

        addresses_file = os.getenv("ADDRESSES_FILE")
        logs_dir = os.getenv("LOGS_DIR")

        if addresses_file is None or logs_dir is None:
            logging.error("A config field is missing!")
            raise MissingConfigField
        
        return Config(addresses_file=Path(addresses_file), logs_dir=Path(logs_dir))