"""
Misc utils for this project.

:author: guylev38
:date: 13/12/2025
"""

# ----- Imports ----- #

import logging
from pathlib import Path
from datetime import date

# ----- Consts ----- #

LOG_FORMAT = (
    "[%(asctime)s] "
    "[%(funcName)s@%(module)s:%(lineno)d] "
    "[%(levelname)s] "
    "%(message)s"
)

DATE_FMT = "%d-%m-%Y %H:%M:%S"


# ----- Functions ----- #


def setup_logger(logs_dir: Path):

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FMT)

    log_filename = f"{date.today().day}-{date.today().month}-{date.today().year}.log"
    file_handler = logging.FileHandler(filename=logs_dir / log_filename, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)