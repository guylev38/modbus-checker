"""
This file contains the config model.

:author: guylev38
:date: 26/12/2025
"""

# ----- Imports ----- #

from pydantic import BaseModel
from pathlib import Path

# ----- Classes ----- #


class Config(BaseModel):
    addresses_file: Path
    logs_dir: Path
