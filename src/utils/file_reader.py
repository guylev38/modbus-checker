"""
File reader utils for this project.

:author: guylev38
:date: 13/12/2025
"""

# ----- Imports ----- # 

from pathlib import Path

# ----- Functions ----- #


def process_file(filepath: Path) -> list[str]:
    """
    Docstring for process_file
    
    :param file: Description
    :return: Description
    """

    with open(filepath.absolute(), "r") as file:
        raw_data = file.readlines()
        data = [line.strip() for line in raw_data]
    
    return data