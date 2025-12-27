"""
Modbus connection checker.

:author: guylev38
:date: 13/12/2025
"""

# ----- Imports ----- #

import logging
import asyncio
from pathlib import Path

from utils.misc import setup_logger
from utils.modbus_checker import ModbusChecker
from utils.config_reader import ConfigReader
from utils.file_reader import process_file
from utils.modbus_factory import ModbusFactory
from models.modbus_device import ModbusDevice
from models.config import Config

# ----- Functions ----- #


def create_devices(addr_filepath: Path) -> list[ModbusDevice]:
    """
    Creates the modbus devices from the config file.
    """
    
    addrs = process_file(addr_filepath)
    return ModbusFactory.create_many(addrs) 


async def main():
    config: Config = ConfigReader.read_config()
    setup_logger(config.logs_dir)
    logging.debug(f"Starting MODBUS_CHECKER. Addresses file: {config.addresses_file} | Logs directory: {config.logs_dir}")

    checker = ModbusChecker(create_devices(config.addresses_file))
    devices = await checker.check()

    for device in devices:
        logging.debug(f"Device: {device.ip}, {device.status}")
    

# ----- Main Entry Point ----- #

if __name__ == "__main__":
    asyncio.run(main())