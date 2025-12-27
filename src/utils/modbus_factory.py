"""
This file contains a modbus factory class.

:author: guylev38
:date: 26/12/2025
"""

# ----- Imports ----- #

from models.modbus_device import ModbusDevice

# ----- Classes ----- #


class ModbusFactory:
    """
    This class creates ModbusDevice classes.
    """

    @classmethod
    def create_single(cls, ip: str) -> ModbusDevice:
        return ModbusDevice(ip=ip)

    @classmethod 
    def create_many(cls, addrs: list[str]) -> list[ModbusDevice]:
        return [cls.create_single(addr) for addr in addrs]